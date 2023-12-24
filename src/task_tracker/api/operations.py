from typing import List
from fastapi import APIRouter
from src.task_tracker.database import get_db
from src.task_tracker.models.schemas import EmployeeBase, TaskBase, TaskCreate
from src.task_tracker import tables
from fastapi import Depends
from sqlalchemy.orm import Session
from src.task_tracker.services.operations import TaskService
from src.task_tracker.tables import Task

router = APIRouter()


@router.get("/")
def read_root():
    return {"200 OK": "Проект запущен"}



# CRUD для Tasks
@router.get("/tasks/")
def read_tasks(service: TaskService = Depends()):
    """Получаем список существующих задач"""
    return service.get_list()

@router.post("/task/create")
def create_task(
        task_data: TaskCreate,
        service: TaskService = Depends()
):
    return service.create_task(task_data)