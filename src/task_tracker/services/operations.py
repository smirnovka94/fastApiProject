from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.task_tracker import tables
from src.task_tracker.database import get_db
from src.task_tracker.models.schemas import TaskCreate, TaskUpdate


class TaskService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_list(self) -> List[tables.Task]:
        """Получение списка задач"""
        return self.db.query(tables.Task).all()

    def _get(self, task_id: int) -> tables.Task:
        task_value = self.db.query(tables.Task).filter(tables.Task.id == task_id).first()
        if not task_value:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return task_value

    def create_task(self, task: TaskCreate) -> tables.Task:
        """Создание задачи"""
        db_task = tables.Task(**task.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_task(self, task_id: int):
        """Получение информации о задаче по id"""
        return self._get(task_id)

    def update_task(self, task_id: int, task_data: TaskUpdate) -> tables.Task:
        """Обновление информации о задаче"""
        task = self._get(task_id)

        for key, value in task_data:
            setattr(task, key, value)

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int):
        """Удаление задачи"""
        task = self._get(task_id)

        self.db.delete(task)
        self.db.commit()
