from enum import Enum
from pydantic import BaseModel
from typing import Optional


class StatusEnum(str, Enum):
    """Варианты статуса задач"""
    active = "free"
    working = "active"
    stoped = "stoped"
    closed = "closed"


class TaskBase(BaseModel):
    name: str
    time_limit_hours: int
    # Валидация status
    status: Optional[StatusEnum]
    related_task: Optional[int] = None
    employee: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class EmployeeBase(BaseModel):
    first_name: str
    second_name: str
    patronymic_name: Optional[str] = None
    position: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass
