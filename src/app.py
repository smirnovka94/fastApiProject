from fastapi import FastAPI
from task_tracker.api import router
import uvicorn
from src.task_tracker.settings import settings

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        'app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
