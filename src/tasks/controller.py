"""
controller.py

Purpose:
--------
This file contains business logic for "Task" operations.

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


from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Path, HTTPException, Query
from src.user.models import UserModel

def create_task(body: TaskSchema, db: Session, user: UserModel):

    # Convert incoming request data to dictionary
    data = body.model_dump()

    # Create a new ORM object (represents a DB row)
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        # Use .get() to avoid crash if field is missing
        is_completed=data.get("is_completed", False),
        user_id = user.id

    )

    # Add object to DB session (not yet saved)
    db.add(new_task)

    # Commit transaction → actually saves to DB
    db.commit()

    # Refresh object → fetch latest data (like auto-generated ID)
    db.refresh(new_task)

    # Return response
    return new_task

def get_task_list(db:Session, user: UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks
    # return JSONResponse(
    #     status_code=200,
    #     content={
    #         "message": "All Task List",
    #         "data": tasks
    #     }
    # )

def get_task_details(task_id: int, db:Session):
    # data = db.query(TaskModel).get(task_id)
    # Correct way in SQLAlchemy 2.0
    data = db.get(TaskModel, task_id)

    # If task not found
    if not data:
        raise HTTPException(status_code=404, detail="Task not found!")

    return data

def update_task(body: TaskSchema, task_id:int, db:Session, user: UserModel):
    # Fetch task from DB
    data:TaskModel | None = db.get(TaskModel, task_id)

    if not data:
        raise HTTPException(status_code=404, detail="Task not found!")

    # Ensure proper comparison (both should be plain values, not column objects)
    if data.user_id != user.id:
        raise HTTPException(status_code=404, detail="You are not allowed to update this!")

    # Convert request body to dict
    updated_data = body.model_dump()

    # Update ORM object fields
    for field, value in updated_data.items():
        setattr(data, field, value)   # setattr() is a built-in Python function used to set (assign) a value to an object’s attribute dynamically
    """Before:
        data.title = "Old"

        After:
        setattr(data, "title", "New")

        Result:
        data.title = "New"
    """

    # Save changes
    db.add(data)
    db.commit()
    db.refresh(data)

    return updated_data

def delete_taks(task_id:int, db:Session, user: UserModel):
    data:TaskModel | None = db.get(TaskModel, task_id)

    if not data:
        raise HTTPException(status_code=404, detail="Task not found!")

        # Ensure proper comparison (both should be plain values, not column objects)
    if data.user_id != user.id:
        raise HTTPException(status_code=404, detail="You are not allowed to delete this!")

    db.delete(data)
    db.commit()

    return None


