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


# TODO: add log events
@router.post("/", response_model=schemas.Course)
def create_course(
    *, db: Session = Depends(depends.get_db), course_in: schemas.CourseCreateAPI,
) -> Any:
    """
    Create Course

    @timeslot_ids: List of timeslot ids in the database, use /timeslot/translate to get these ids.
    """
    # Retrieve corresponding timeslot objects
    timeslot_ids = course_in.timeslot_ids
    timeslots = crud.course_timeslot.get_multi_by_id(db=db, ids=timeslot_ids)

    num_timeslot_required, num_timeslot_actual = len(set(timeslot_ids)), len(timeslots)
    if num_timeslot_required != num_timeslot_actual:
        missing = set(timeslot_ids) - set([t.id for t in timeslots])
        raise HTTPException(status_code=404, detail=f"Timeslots not exist: {missing}")

    # If there exists one course with the same permanent id but different info
    #   response with error
    # TODO: implement this

    # Create the whole object
    course_to_create = {**course_in.dict(exclude={"timeslot_ids"})}
    course = crud.course.create(db=db, obj_in=course_to_create, timeslots=timeslots)
    return course


# @router.get("/{course_id}", response_model=schemas.Course)
# def read_course_information(
#     *, db: Session = Depends(depends.get_db), course_id: int,
# ) -> Any:
#     """
#     read course info
#     """
#     course = crud.course.get(db, id=course_id)
#     if not course:
#         raise HTTPException(
#             status_code=404,
#             detail="The course with this id does not exist in the system",
#         )
#     return course


# @router.patch("/{course_id}", response_model=schemas.Course)
# def update_course(
#     *,
#     db: Session = Depends(depends.get_db),
#     course_id: int,
#     course_in: schemas.CourseUpdateAPI,
# ) -> Any:
#     """
#     Update fields of a course object.
#     """

#     course = crud.course.get(db, id=course_in.id)
#     if not course:
#         raise HTTPException(
#             status_code=404,
#             detail="The course with this name does not exist in the system",
#         )
#     course = crud.course.update(db, db_obj=course, obj_in=course_in)
#     return course


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
