import os
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    server_host: str = os.getenv('SERVER_HOST')
    server_port: int = os.getenv('SERVER_PORT')
    database_url: str = os.getenv('DB_POSTGRES')


settings = Settings()
