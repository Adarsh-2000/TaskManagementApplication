from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import Dict, Optional, Annotated, Literal

class TaskSchema(BaseModel):
    title: Annotated[str, Field(...)]
    description: Annotated[Optional[str], Field(default=None)]
    is_completed: Annotated[Optional[bool], Field(default=False,)]


class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    user_id: int | None = 0