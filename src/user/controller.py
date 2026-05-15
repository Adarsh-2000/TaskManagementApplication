"""
controller.py

Purpose:
--------
This file contains business logic for "User" operations.

Why we use a controller layer:
------------------------------
- Keeps API routes clean (no heavy logic in routes)
- Separates business logic from request handling
- Makes code more modular and maintainable
- Easier to test independently

Responsibilities:
-----------------
- Handle CRUD operations (Create, Read, Update, Delete)
- Interact with the database using SQLAlchemy ORM
- Process and transform data if needed
- Return appropriate responses

Usage:
------
These functions are called from route files.

Example:
    from src.tasks import controller

    @task_routes.post("/create")
    def create_task(body: TaskSchema, db: Session = Depends(get_db)):
        return controller.create_task(body, db)
"""


from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Path, HTTPException, Query
from pwdlib import PasswordHash
from fastapi import APIRouter, Depends, status, Request
import jwt
from src.utils.settings import settings
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidAlgorithmError
from jose.exceptions import JWTError, ExpiredSignatureError


password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)



def register_user(body: UserSchema, db: Session):
    """
    Register a new user
    """

    # Check if username already exists
    existing_user = db.query(UserModel).filter(
        UserModel.username == body.username
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Check if email already exists
    existing_email = db.query(UserModel).filter(
        UserModel.email == body.email
    ).first()

    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Hash password
    hashed_password = get_password_hash(body.password)

    # Create new user
    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=hashed_password,
        email=body.email
    )

    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(body: LoginSchema, db: Session):
    """
    Login user and generate JWT token

    Flow:
    -----
    1. Check if user exists in DB
    2. Verify password (hashed comparison)
    3. Generate JWT token
    4. Return token to client
    """

    # ===============================
    # STEP 1: CHECK USER EXISTS
    # ===============================
    existing_user = db.query(UserModel).filter(
        UserModel.username == body.username
    ).first()

    # If username not found → Unauthorized
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You entered wrong username!"
        )

    # ===============================
    # STEP 2: VERIFY PASSWORD
    # ===============================
    # Compare plain password (input) with hashed password (DB)
    if not verify_password(body.password, existing_user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You entered wrong password!"
        )

    # ===============================
    # STEP 3: GENERATE JWT TOKEN
    # ===============================
    # Payload = data stored inside token
    payload = {
        "_id": existing_user.id,   # storing user id inside token
        "exp": datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    # Create token using:
    # - payload (user data)
    # - SECRET_KEY (used to sign token)
    # - ALGORITHM (encryption algorithm like HS256)
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    # ===============================
    # STEP 4: RETURN TOKEN
    # ===============================
    return {"token": token}
    # return {
    #     "access_token": token,
    #     "token_type": "bearer"
    # }


def is_authenticated(request: Request, db:Session):
    try:
        print(request.headers)

        token = request.headers.get("authorization") or request.query_params.get("Authorization")

        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized! 1")

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = data.get("_id")

        user = db.query(UserModel).filter(
            UserModel.id == user_id
        ).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized! 3")

        return user

    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized! 3")

