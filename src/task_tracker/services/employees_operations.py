from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.task_tracker import tables
from src.task_tracker.database import get_db
from src.task_tracker.models.schemas import EmployeeCreate, EmployeeUpdate
from src.task_tracker.tables import Task


class EmployeeService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_list(self) -> List[tables.Employee]:
        """Получение списка сотрудников"""
        return self.db.query(tables.Employee).all()

    def _get(self, employee_id: int) -> tables.Employee:
        employee_value = self.db.query(tables.Employee).filter(tables.Employee.id == employee_id).first()
        if not employee_value:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return employee_value

    def create_employee(self, employee: EmployeeCreate) -> tables.Employee:
        """Создание сотрудника"""
        db_employee = tables.Employee(**employee.dict())
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee

    def get_employee(self, employee_id: int):
        """Получение информации о сотруднике по id"""
        return self._get(employee_id)

    def update_employee(self, employee_id: int, employee_data: EmployeeUpdate) -> tables.Employee:
        """Обновление информации о задаче"""
        employee = self._get(employee_id)

        for key, value in employee_data:
            setattr(employee, key, value)

        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete_employee(self, employee_id: int):
        """Удаление сотрудника"""
        employee = self._get(employee_id)

        self.db.delete(employee)
        self.db.commit()

    def get_busy_employees(self, status="active"):
        """Получение списка занятых сотрудников"""
        employees = self.db.query(tables.Employee).all()

        dict_employee_task_count = dict()
        for employee in employees:
            # Количество активных задач
            task_count = (self.db.query(tables.Task)
                          .filter((Task.employee == employee.id) and (tables.Task.status == status))
                          .count())
            employee.task_count = task_count
            # Список активных задач
            tasks = (self.db.query(tables.Task)
                     .filter((tables.Task.employee == employee.id) & (tables.Task.status == status))
                     .all())
            employee.tasks = tasks

            task_sum = []
            for task in tasks:
                task_sum.append(task)
            dict_employee_task_count.setdefault(employee, []).append(task_count)
            sorted_dict = sorted(dict_employee_task_count.items(), key=lambda x: x[1])
        sort_employees = []
        for key, value in sorted_dict:
            sort_employees.append(key)

        return sort_employees
