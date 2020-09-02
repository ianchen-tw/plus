from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import depends
from app.core import timeslot_parser

router = APIRouter()


@router.get("/", response_model=List[schemas.Course])
def get_list_of_courses(
    db: Session = Depends(depends.get_db), skip: int = 0, limit: int = 100
) -> List[Any]:
    """ Get all information of all courses"""
    courses = crud.course.get_multi(db)
    return courses


# TODO: add log events
@router.post("/", response_model=schemas.Course)
def create_course(
    *, db: Session = Depends(depends.get_db), course_in: schemas.CourseCreateAPI,
) -> Any:
    """
    Create Course
    """
    # extract base information inside a course
    base_info_of_new_course = schemas.CourseCreate(**dict(course_in))

    course_orm_obj = crud.course.find_by_permanent_id(
        db, pid=base_info_of_new_course.permanent_id
    )

    if course_orm_obj:
        # if the same: return the same object
        in_db = schemas.CourseInDB.from_orm(course_orm_obj)
        converted = schemas.CourseCreate(**dict(in_db))
        if base_info_of_new_course == converted:
            return course_orm_obj

        # else report error
        # TODO: compare and show the data inside database
        raise HTTPException(
            status_code=409,
            detail="Permanent_id have been used with different course content, use /course/update instead.",
        )
    else:
        # course_in.timeslots is actually a timeslot_exp but not timeslots
        timeslot_exp = course_in.timeslots
        timeslots_internal = timeslot_parser.parse_timeslots(exp=timeslot_exp)
        course = crud.course.create(
            db=db, obj_in=base_info_of_new_course, timeslots_internal=timeslots_internal
        )
        return course


@router.get("/{course_id}", response_model=schemas.Course)
def read_course_information(
    *, db: Session = Depends(depends.get_db), course_id: int,
) -> Any:
    """
    read course info
    """
    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with this id does not exist in the system",
        )
    return course


@router.patch("/{course_id}", response_model=schemas.Course)
def update_course(
    *,
    db: Session = Depends(depends.get_db),
    course_id: int,
    course_in: schemas.CourseUpdateAPI,
) -> Any:
    """
    Update fields of a course object.

    Provide partial fields would partially update a course object
    """

    course_orm_obj = crud.course.get(db, id=course_id)
    if not course_orm_obj:
        raise HTTPException(
            status_code=404,
            detail="The course with this name does not exist in the system",
        )

    provided_timeslot_exp = course_in.timeslots
    provided_timeslots_internal = []
    if provided_timeslot_exp != None:
        provided_timeslots_internal = timeslot_parser.parse_timeslots(
            exp=provided_timeslot_exp
        )

    course_update = schemas.CourseUpdate(**dict(course_in))
    course = crud.course.update(
        db=db,
        course=course_orm_obj,
        obj_in=course_update,
        new_timeslots_internal=provided_timeslots_internal,
    )
    return course


@router.delete("/{course_id}", response_model=schemas.Course)
def remove_course(*, db: Session = Depends(depends.get_db), course_id: int,) -> Any:
    """
    [Dangerous] Remove a course object
    """

    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with this name does not exist in the system",
        )
    course = crud.course.remove(db, id=course_id)
    return course
