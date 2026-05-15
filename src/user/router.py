"""
user_routes.py

Purpose:
--------
This file defines API routes related to "User".

Why we use APIRouter:
---------------------
- Keeps routes modular (separate from main.py)
- Helps organize large applications
- Allows grouping related endpoints (e.g., all user APIs)

Usage:
------
This router will be included in main.py using:
    app.include_router(user_routes)
"""

from fastapi import APIRouter, Depends, status, Request
from src.user import controller
from src.user.dtos import UserSchema, UserResponseSchema, LoginSchema, LoingResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List

# Create a router instance for task-related APIs
user_routes = APIRouter(
    prefix="/user"  # All endpoints will start with /tasks
    # Example:
    # GET /tasks
    # POST /tasks
    # GET /tasks/{id}
)

@user_routes.post('/register', response_model= UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register_user(body: UserSchema, db:Session = Depends(get_db)):
    return controller.register_user(body=body, db=db)

@user_routes.post('/login',status_code=status.HTTP_200_OK)
def login_user(body:LoginSchema, db:Session = Depends(get_db)):
    return controller.login_user(body=body, db=db)

@user_routes.get('/auth',response_model = LoingResponseSchema ,status_code=status.HTTP_200_OK)
def is_authenticated(request: Request, db:Session = Depends(get_db)):
    return controller.is_authenticated(request = request, db = db)