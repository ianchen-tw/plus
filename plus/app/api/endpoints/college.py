from typing import Any, List

from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter

from app import schemas
from app.api import depends


router = APIRouter()


@router.post("/", response_model=List[schemas.College])
def get_colleges(
    *, db: Session = Depends(depends.get_db), college: schemas.College,
) -> List[Any]:
    """ Get all information of all colleges"""
    c1 = college.copy()
    c1.name = "test"
    return [college,c1, college]

    # return {"message": "collages"}
