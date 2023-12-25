from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from src.task_tracker.models.schemas import TaskCreate, TaskUpdate
from src.task_tracker.services.operations import TaskService


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


@router.get("/task/{task_id}")
def read_task(
        task_id: int,
        service: TaskService = Depends()
):
    return service.get_task(task_id)


@router.put("/task/{task_id}")
def update_task(
        task_id: int,
        task_data: TaskUpdate,
        service: TaskService = Depends()
):
    return service.update_task(task_id, task_data)


@router.delete("/task/{task_id}")
def delete_task(
        task_id: int,
        service: TaskService = Depends()
):
    service.delete_task(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
