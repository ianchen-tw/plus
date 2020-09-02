from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.course_timeslot import CourseTimeslot
from app.schemas.course_timeslot import CourseTimeslotCreate, CourseTimeslotUpdate
from ..core.timetable import TimeSlot


class CRUDCourseTimeSlot(
    CRUDBase[CourseTimeslot, CourseTimeslotCreate, CourseTimeslotUpdate]
):
    def get_multi_by_id(self, db: Session, *, ids: List[int]) -> List[CourseTimeslot]:
        timeslots = db.query(self.model).filter(self.model.id.in_(ids)).all()
        return timeslots

    def find_timeslots(
        self, db: Session, *, timeslots: List[TimeSlot]
    ) -> List[CourseTimeslot]:
        slot = []
        for ts in timeslots:
            cts = (
                db.query(self.model)
                .filter(
                    and_(
                        self.model.kind == ts.kind,
                        self.model.code == ts.code,
                        self.model.timespan == ts.timespan,
                        self.model.weekday == ts.weekday,
                    )
                )
                .all()
            )
            slot.extend(cts)
        return slot

    def find_timeslot(self, db: Session, *, timeslot: TimeSlot) -> CourseTimeslot:
        existed_timeslot = (
            db.query(self.model)
            .filter(
                and_(
                    self.model.kind == timeslot.kind,
                    self.model.code == timeslot.code,
                    self.model.timespan == timeslot.timespan,
                    self.model.weekday == timeslot.weekday,
                )
            )
            .first()
        )
        return existed_timeslot


course_timeslot = CRUDCourseTimeSlot(CourseTimeslot)
