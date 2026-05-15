"""
main.py

Purpose:
--------
Entry point of the FastAPI application.

Responsibilities:
-----------------
1. Create FastAPI app instance
2. Include routers (API endpoints)
3. Initialize resources (DB, cache, etc.)
4. Handle startup & shutdown events
"""
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.utils.db import Base, engine
from src.tasks.router import task_routes
from src.user.router import user_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan function handles:
    - App startup
    - App shutdown
    """

    # ===============================
    # STARTUP LOGIC
    # ===============================
    print("App is starting...")

    # Create DB tables (only for development)
    # This will create all tables defined using ORM models
    # (only if they don't already exist in the database)
    Base.metadata.create_all(bind=engine)

    yield  # 👈 App runs here

    # ===============================
    # SHUTDOWN LOGIC
    # ===============================
    print("App is shutting down...")

# Pass lifespan to FastAPI
app = FastAPI(title="Task Management Application",lifespan=lifespan)
app.include_router(task_routes)
app.include_router(user_routes)


# from fastapi import FastAPI
# from src.utils.db import Base, engine

# Base.metadata.create_all(engine)

# app = FastAPI(title="This is Taks Management Application")