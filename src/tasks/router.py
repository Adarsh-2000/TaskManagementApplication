"""
task_routes.py

Purpose:
--------
This file defines API routes related to "Task".

Why we use APIRouter:
---------------------
- Keeps routes modular (separate from main.py)
- Helps organize large applications
- Allows grouping related endpoints (e.g., all task APIs)

Usage:
------
This router will be included in main.py using:
    app.include_router(task_routes)
"""

from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List
from src.utils.helper import is_authenticated
from src.user.models import UserModel

# Create a router instance for task-related APIs
task_routes = APIRouter(
    prefix="/tasks"  # All endpoints will start with /tasks
    # Example:
    # GET /tasks
    # POST /tasks
    # GET /tasks/{id}
)

@task_routes.post('/create', response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.create_task(body, db, user)

@task_routes.get('/list', response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_task_list(db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.get_task_list(db = db, user=user)

@task_routes.get('/details/{task_id}',response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_task_details(task_id:int, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.get_task_details(task_id, db = db)

@task_routes.put('/update/{task_id}',response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task(body: TaskSchema, task_id:int, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.update_task(body=body, task_id=task_id, db=db, user= user)

@task_routes.delete('/delete/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_taks(task_id:int, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.delete_taks(task_id=task_id, db=db, user = user)
