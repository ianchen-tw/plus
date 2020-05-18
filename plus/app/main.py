import logging

from fastapi import (
    FastAPI,
    Query,
)
from app.api.main_router import main_router
from pydantic import BaseModel

from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TODO: load dynamic setting, to be able to run in production

server = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
)
server.include_router(main_router)
