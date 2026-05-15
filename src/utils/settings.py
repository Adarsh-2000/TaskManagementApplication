"""
settings.py

Why this file exists:
---------------------
This file centralizes all configuration of the application.

Instead of hardcoding values (like database URLs, API keys, debug flags),
we store them in environment variables (.env file or system env),
and load them here using Pydantic.

Benefits:
---------
1. Security → Sensitive data (passwords, DB URLs) are not hardcoded
2. Flexibility → Easily switch between dev / staging / production
3. Clean code → No scattered config across files
4. Maintainability → Single source of truth

How it's used:
--------------
- Import `settings` anywhere in your app
- Access values like: settings.DB_CONNECTION

Example:
    from settings import settings
    db_url = settings.DB_CONNECTION
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration class.

    Automatically reads:
    - .env file
    - System environment variables

    Priority:
    1. System environment variables
    2. .env file
    3. Default values (defined below)
    """

    # Configuration for Pydantic Settings
    model_config = SettingsConfigDict(
        env_file=".env",   # Load variables from .env file
        extra="ignore"     # Ignore extra variables not defined here
    )

    # ===============================
    # DATABASE CONFIGURATION
    # ===============================
    DB_CONNECTION: str = ""
    # Example:
    # postgresql://user:password@localhost:5432/db_name

    SECRET_KEY:str = ""
    ALGORITHM:str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES:int=0
    # ===============================
    # APPLICATION SETTINGS
    # ===============================
    # APP_NAME: str = "FastAPI App"
    # DEBUG: bool = False


# Singleton instance (used across the app)
settings = Settings()