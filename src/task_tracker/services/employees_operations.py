from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.task_tracker import tables
from src.task_tracker.database import get_db
from src.task_tracker.models.schemas import EmployeeCreate, EmployeeUpdate


class EmployeeService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_list(self) -> List[tables.Employee]:
        """Получение списка задач"""
        return self.db.query(tables.Employee).all()

    def _get(self, employee_id: int) -> tables.Employee:
        employee_value = self.db.query(tables.Employee).filter(tables.Employee.id == employee_id).first()
        if not employee_value:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return employee_value

    def create_employee(self, employee: EmployeeCreate) -> tables.Employee:
        """Создание задачи"""
        db_employee = tables.Employee(**employee.dict())
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee

    def get_employee(self, employee_id: int):
        """Получение информации о задаче по id"""
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
        """Удаление задачи"""
        employee = self._get(employee_id)

        self.db.delete(employee)
        self.db.commit()
