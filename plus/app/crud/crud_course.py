from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.core.objects import CodedTimeInterval
from app.crud.base import CRUDBase
from app.models.course import Course
from app.models.course_timeslot import CourseTimeslot
from app.schemas.course import CourseCreate, CourseUpdate
from app.schemas.course_timeslot import CourseTimeslotCreate


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):
    def find_by_permanent_id(self, db: Session, *, pid: str) -> Course:
        course = db.query(self.model).filter(self.model.permanent_id == pid).first()
        return course

    def _add_timeslots(
        self,
        db: Session,
        *,
        course: Course,
        time_intervals: List[CodedTimeInterval],
        commit: bool = True,
    ):
        for t in time_intervals:
            arg_dict = {**t.as_dict(), "course_id": course.id}
            timeslot_to_create = CourseTimeslotCreate(**arg_dict)
            timeslot_obj = CourseTimeslot(**dict(timeslot_to_create))
            db.add(timeslot_obj)
            db.flush()
            course.timeslots.append(timeslot_obj)
        if commit:
            db.commit()

    # override the base type
    def create(
        self,
        db: Session,
        *,
        obj_in: CourseCreate,
        time_intervals: List[CodedTimeInterval],
    ) -> Course:
        obj_in_data = jsonable_encoder(obj_in)
        course = self.model(**obj_in_data)  # type: ignore
        db.add(course)

        db.flush()  # generate course.id
        # create timeslots inside base on the internal timeslot format
        self._add_timeslots(
            db=db, course=course, time_intervals=time_intervals, commit=False
        )
        db.commit()
        db.refresh(course)
        return course

    def update(
        self,
        db: Session,
        *,
        course: Course,
        obj_in: CourseUpdate,
        new_timeslots_internal: List[CodedTimeInterval],
    ) -> Course:
        obj_data = jsonable_encoder(course)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(course, field, update_data[field])

        # update timeslots if provided
        if new_timeslots_internal:
            db.query(CourseTimeslot).filter(
                CourseTimeslot.course_id == course.id
            ).delete()
            self._add_timeslots(
                db=db, course=course, time_intervals=new_timeslots_internal, commit=False,
            )
        db.add(course)
        db.commit()
        db.refresh(course)
        return course


course = CRUDCourse(Course)
