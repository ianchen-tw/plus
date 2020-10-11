from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import depends

router = APIRouter()


@router.get("/", response_model=List[schemas.CourseTimeslotInDB])
def get_list_of_timeslots(
    db: Session = Depends(depends.get_db), skip: int = 0, limit: int = 100
) -> List[Any]:
    """ Get all information of all c_timeslots"""
    timeslots = crud.course_timeslot.get_multi(db)
    return timeslots


@router.get("/{timeslot_id}", response_model=schemas.CourseTimeslotInDB)
def read_timeslot_information(
    *, db: Session = Depends(depends.get_db), timeslot_id: int,
) -> Any:
    """
    read timeslot info
    """
    timeslot = crud.course_timeslot.get(db, id=timeslot_id)
    if not timeslot:
        raise HTTPException(
            status_code=404,
            detail="The timeslot with this id does not exist in the system",
        )
    return timeslot
