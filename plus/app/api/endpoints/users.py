from typing import Any

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def get_users() -> Any:
    return {"message": "user"}
