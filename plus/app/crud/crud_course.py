from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas
from app.crud.base import CRUDBase
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):

    # override the base type
    def create(
        self,
        db: Session,
        *,
        obj_in: CourseCreate,
        timeslots: List[schemas.CourseTimeslot]
    ) -> Course:
        obj_in_data = jsonable_encoder(obj_in)
        course = self.model(**obj_in_data)  # type: ignore
        course.timeslots.extend(timeslots)
        db.add(course)
        db.commit()
        db.refresh(course)
        return course


course = CRUDCourse(Course)
