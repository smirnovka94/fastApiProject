# Описание проекта
Проект серверного приложения для работы с базой данных для анализа работы сотрудников
База данных - Postgres
БД представляет собой трекер задач и содержит следующие таблицы:

1)Таблица сотрудников (ФИО, должность);

2)Таблица задач (наименование, ссылка на родительскую задачу, если есть зависимость, исполнитель, срок, статус).

### Хранятся эндпоинты по пути
src/task_tracker/api

### Хранится бизнес логика по пути
src/task_tracker/services

### Хранятся модели по пути
src/task_tracker/models

# Запуск проекта

### скопировать репозиторий
```
git clone https://github.com/smirnovka94/fastApiProject.git
```
### установить виртуальное окружение
```
python -m venv venv
```
### установить библиотеки
```
pip install -r src\requirements.txt
```
### создать базу данных в PgAdmin с именем <fast_task_traker>

### создать файл <.env> из <.env.template>
Внутри .env заменить password на пароль Postgress

### копируем значение DB_POSTGRES= в файл alembic.ini. заполняем параметр sqlalchemy.url = 

### добавляем текущую директорию в переменную среды 
для Linux
```
export PYTHONPATH="$PYTHONPATH:$PWD"
```
для Windows
```
set PYTHONPATH=%PYTHONPATH%;%CD%
```
### Создаем миграции
```
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head        
```
### Запуcтить приложение
```
venv\Scripts\python.exe src\app.py
```
