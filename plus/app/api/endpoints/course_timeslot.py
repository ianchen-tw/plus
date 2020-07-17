from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import depends

router = APIRouter()


@router.get("/", response_model=List[schemas.CourseTimeslot])
def get_list_of_timeslots(
    db: Session = Depends(depends.get_db), skip: int = 0, limit: int = 100
) -> List[Any]:
    """ Get all information of all c_timeslots"""
    timeslots = crud.course_timeslot.get_multi(db)
    return timeslots


@router.post("/", response_model=schemas.CourseTimeslot)
def create_timeslot(
    *, db: Session = Depends(depends.get_db), timeslot: schemas.CourseTimeslotCreate,
) -> Any:
    """
    Create CourseTimeslot
    """
    ts = crud.course_timeslot.create(db=db, obj_in=timeslot)
    return ts


@router.get("/{timeslot_id}", response_model=schemas.CourseTimeslot)
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


@router.patch("/{timeslot_id}", response_model=schemas.CourseTimeslot)
def update_timeslot(
    *,
    db: Session = Depends(depends.get_db),
    timeslot_id: int,
    timeslot_in: schemas.CourseTimeslotUpdate,
) -> Any:
    """
    Update fields of a timeslot object.
    Will only update the field you prvide.
    """

    timeslot = crud.course_timeslot.get(db, id=timeslot_id)
    if not timeslot:
        raise HTTPException(
            status_code=404,
            detail="The timeslot with this name does not exist in the system",
        )
    timeslot = crud.course_timeslot.update(db, db_obj=timeslot, obj_in=timeslot_in)
    return timeslot


@router.delete("/{timeslot_id}", response_model=schemas.CourseTimeslot)
def remove_timeslot(*, db: Session = Depends(depends.get_db), timeslot_id: int,) -> Any:
    """
    [Dangerous] Remove a timeslot object
    """

    timeslot = crud.course_timeslot.get(db, id=timeslot_id)
    if not timeslot:
        raise HTTPException(
            status_code=404,
            detail="The timeslot with this name does not exist in the system",
        )
    timeslot = crud.course_timeslot.remove(db, id=timeslot_id)
    return timeslot
