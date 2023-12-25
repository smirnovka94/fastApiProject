from fastapi import APIRouter
from .routers import router as operation_router

router = APIRouter()
router.include_router(operation_router)