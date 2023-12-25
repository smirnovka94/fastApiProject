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

    def get_important_tasks(self, ):
        """Получаем список важных задач"""

        employees = self.db.query(tables.Employee).all()
        all_tasks = self.db.query(tables.Task).all()
        sub_tasks = (self.db.query(tables.Task)
                     .filter(tables.Task.related_task != None)
                     .all()
                     )

        id_parrent_tasks = []
        id_employee_with_parrent_tasks = []

        for sub_task in sub_tasks:
            # Получаем id родительской задачи
            id_parrent_tasks.append(sub_task.related_task)

        for task in all_tasks:
            if (task.id in id_parrent_tasks) and (task.employee != None):
                id_employee_with_parrent_tasks.append(task.employee)

        # Самый свободный сотрудник
        count_tasks = 100000000
        count_tasks_p = 100000000
        for employee in employees:
            # Ищем количество задач у сотрудника
            tasks = (self.db.query(tables.Task)
                     .filter(tables.Task.employee == employee.id)
                     .all()
                     )
            employee.tasks = len(tasks)
            # Находим наименее занятого
            if int(employee.tasks) < count_tasks:
                count_tasks = len(tasks)
                free_employee = employee

            # Ищем незагруженного сотрудника с родительскими задачами
            if employee.id in id_employee_with_parrent_tasks:
                if int(employee.tasks) < count_tasks_p:
                    count_tasks_p = employee.tasks
                    free_employee_with_parrent_tasks = employee

        # Ищем наиболее подходящего кандидата
        if int(free_employee_with_parrent_tasks.tasks) <= int(free_employee.tasks) + 2:
            ideal_employee = free_employee_with_parrent_tasks
        else:
            ideal_employee = free_employee

        # Получаем свободные задачи
        important_tasks = []
        tasks_active = (self.db.query(tables.Task)
                        .filter(tables.Task.status == "free")
                        .all()
                        )
        for task in tasks_active:
            if task.id in id_parrent_tasks:
                if ideal_employee.patronymic_name == None:
                    task.employees = [ideal_employee.first_name, ideal_employee.second_name]
                else:
                    task.employees = [ideal_employee.first_name, ideal_employee.second_name,
                                      ideal_employee.patronymic_name]
                filter_task = {"Важная задача": task.name, "Срок": task.time_limit_hours,
                               "ФИО сотрудника": task.employees}
                important_tasks.append(filter_task)

        return important_tasks
