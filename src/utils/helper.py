from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Path, HTTPException, Query, Depends
from pwdlib import PasswordHash
from fastapi import APIRouter, Depends, status, Request
from src.utils.db import get_db
import jwt
from src.utils.settings import settings
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidAlgorithmError
from jose.exceptions import JWTError, ExpiredSignatureError


def is_authenticated(request: Request, db:Session = Depends(get_db)):
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