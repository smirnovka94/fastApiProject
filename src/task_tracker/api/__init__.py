from fastapi import APIRouter
from .routers import router as operation_router
from .functions import router as functions


router = APIRouter()
router.include_router(operation_router)
router.include_router(functions)
