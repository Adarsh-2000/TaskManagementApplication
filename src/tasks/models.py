"""
task_model.py

Purpose:
--------
This file defines the ORM(Object Relational Mapping) model for "Task".

What it does:
-------------
- Maps a Python class to a database table
- Defines table structure (columns, types, defaults)

How it's used:
--------------
- SQLAlchemy uses this to create tables in DB
- Used in CRUD operations (create, read, update, delete)

Example usage:
--------------
new_task = TaskModel(title="Learn FastAPI", description="Study ORM")
db.add(new_task)
db.commit()
"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from src.utils.db import Base


class TaskModel(Base):
    """
    ORM model for tasks.

    This class represents the "user_tasks" table in the database.
    """

    # Name of the table in the database
    __tablename__ = "user_tasks"

    # ===============================
    # COLUMNS (table fields)
    # ===============================

    # Primary key (unique ID for each task)
    id = Column(Integer, primary_key=True)

    # Task title (short text)
    title = Column(String)

    # Task description (longer text)
    description = Column(String)

    # Boolean flag to track completion status
    # Default value = False (task is not completed initially)
    is_completed = Column(Boolean, default=False)

    # Foreign key linking this task to a specific user
    # References the "id" column in the "user_table"
    # Ensures each task belongs to a valid user (one-to-many relationship)
    # ondelete="CASCADE" means:
    # → If a user is deleted, all tasks associated with that user
    #   will be automatically deleted by the database
    # → Prevents orphan records (tasks without a valid user)
    user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"))


"""
COLUMN ↓

id | title          | description      | is_completed
----------------------------------------------------
1  | Learn FastAPI  | Study ORM        | False   → ROW →
2  | Build API      | Create endpoints | True

"""
