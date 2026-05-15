"""
user_model.py

Purpose:
--------
This file defines the ORM (Object Relational Mapping) model for "User".

What it does:
-------------
- Maps a Python class to a database table
- Defines table structure (columns, data types, constraints)
- Used by SQLAlchemy to interact with the database

How it's used:
--------------
- SQLAlchemy reads this model to create the table in DB
- Used in CRUD operations (create, read, update, delete)

Example usage:
--------------
new_user = UserModel(
    name="Adi",
    username="adi123",
    hash_password="hashed_password",
    email="adi@test.com"
)

db.add(new_user)
db.commit()
"""

from sqlalchemy import Column, Integer, String
from src.utils.db import Base


class UserModel(Base):
    """
    ORM model for users.

    This class represents the "user_table" in the database.
    Each instance of this class = one row in the table.
    """

    # ===============================
    # TABLE NAME
    # ===============================
    __tablename__ = "user_table"

    # ===============================
    # COLUMNS (table fields)
    # ===============================

    # Primary key (unique ID for each user)
    id = Column(Integer, primary_key=True, index=True)

    # Full name of the user
    name = Column(String, nullable=True)

    # Username (must be provided)
    username = Column(String, nullable=False, unique=True)

    # Hashed password (never store plain password)
    hash_password = Column(String, nullable=False)

    # Email address
    email = Column(String, nullable=True)



"""
COLUMN ↓

id | name | username | hash_password | email
--------------------------------------------
1  | Adi  | adi123   | ******        | adi@test.com
2  | Raj  | raj456   | ******        | raj@test.com

"""