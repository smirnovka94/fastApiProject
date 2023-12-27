from fastapi import APIRouter
from fastapi import Depends

from src.task_tracker.services.employees_operations import EmployeeService
from src.task_tracker.services.tasks_operations import TaskService

router = APIRouter(
    tags=["Functions"],
)


@router.get("/tasks/important")
def get_important_tasks(service: TaskService = Depends()):
    """Получаем список важных задач"""
    items = service.get_important_tasks()
    return items


@router.get("/employees/busy")
def get_busy_employees(service: EmployeeService = Depends()):
    """Получаем список занятых сотрудников"""
    items = service.get_busy_employees()
    return items
