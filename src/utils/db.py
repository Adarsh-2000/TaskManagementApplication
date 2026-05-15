"""
db.py

Purpose:
--------
This file is responsible for:
1. Creating a database connection (engine)
2. Creating a session factory
3. Providing DB sessions to FastAPI routes (dependency)

Why needed:
-----------
- Keeps DB logic separate from business logic
- Reusable across entire application
- Follows clean architecture practices
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings


# Base class for all ORM models / An ORM model is a Python class that represents a database table
# All your database tables will inherit from this
Base = declarative_base()


# ===============================
# DATABASE ENGINE
# ===============================
# Engine is the core interface to the database
engine = create_engine(
    url=settings.DB_CONNECTION,   # Loaded from .env via settings.py
    # echo=settings.DEBUG           # Logs SQL queries if DEBUG=True
)


# ===============================
# SESSION FACTORY
# ===============================
# Creates new DB session instances
SessionLocal = sessionmaker(
    # autocommit=False,   # Changes are committed manually
    # autoflush=False,    # Prevents auto flushing before queries
    bind=engine
)


# ===============================
# DEPENDENCY (used in FastAPI)
# ===============================
def get_db():
    """
    Dependency function to get DB session.

    Usage in FastAPI:
        def route(db: Session = Depends(get_db))

    Flow:
    - Create session
    - Use it in request
    - Close after request ends
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()