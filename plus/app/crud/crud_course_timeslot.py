from app.crud.base import CRUDBase
from app.models.course_timeslot import CourseTimeslot
from app.schemas.course_timeslot import CourseTimeslotCreate, CourseTimeslotUpdate


class CRUDCourseTimeSlot(
    CRUDBase[CourseTimeslot, CourseTimeslotCreate, CourseTimeslotUpdate]
):
    pass


course_timeslot = CRUDCourseTimeSlot(CourseTimeslot)
