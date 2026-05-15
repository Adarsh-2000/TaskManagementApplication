from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Dict, Optional, Annotated, Literal

class UserSchema(BaseModel):
    name: Annotated[str, Field(...)]
    username: Annotated[str, Field(...)]
    password: Annotated[str, Field(...)]
    email: Annotated[EmailStr, Field(...)]


class UserResponseSchema(BaseModel):
    name: str
    username: str
    email: str



class LoginSchema(BaseModel):
    username: str
    password: str

class LoingResponseSchema(BaseModel):
    name: str
    username: str
    email: str



