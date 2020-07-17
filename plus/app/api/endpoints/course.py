from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import depends

router = APIRouter()


@router.get("/", response_model=List[schemas.Course])
def get_list_of_courses(
    db: Session = Depends(depends.get_db), skip: int = 0, limit: int = 100
) -> List[Any]:
    """ Get all information of all courses"""
    courses = crud.course.get_multi(db)
    return courses


@router.post("/", response_model=schemas.Course)
def create_course(
    *, db: Session = Depends(depends.get_db), course: schemas.CourseCreate,
) -> Any:
    """
    Create Course
    """
    c = crud.course.create(db=db, obj_in=course)
    return c


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
    course_in: schemas.CourseUpdate,
) -> Any:
    """
    Update fields of a course object.
    Will only update the field you prvide.
    """

    course = crud.course.get(db, id=course_id)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="The course with this name does not exist in the system",
        )
    course = crud.course.update(db, db_obj=course, obj_in=course_in)
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
