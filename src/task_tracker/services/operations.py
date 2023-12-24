from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.task_tracker import tables
from src.task_tracker.database import get_db
from src.task_tracker.models.schemas import TaskCreate
from src.task_tracker.tables import Task


class TaskService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_list(self) -> List[tables.Task]:
        """Получение списка задач"""
        return self.db.query(tables.Task).all()

    def create_task(self, task: TaskCreate) -> tables.Task:
        """Создание задачи"""
        db_task = tables.Task(**task.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task