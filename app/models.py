from pydantic import BaseModel
from typing import Optional

# Base Model (Shared properties)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True