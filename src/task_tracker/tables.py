from sqlalchemy import Column, ForeignKey, Integer, String, MetaData
from src.task_tracker.database import Base


metadata = MetaData()


class Employee(Base):
    """Модель сотрудников"""
    __tablename__ = "employees"

    metadata1 = metadata
    id = Column("id", Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    patronymic_name = Column(String, nullable=True)
    position = Column(String)


class Task(Base):
    """Модель задач"""
    __tablename__ = "tasks"

    metadata2 = metadata
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    related_task = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    employee = Column(Integer, ForeignKey("employees.id"), nullable=True)
    time_limit_hours = Column(Integer)
    status = Column(String, nullable=False, default="waiting")
