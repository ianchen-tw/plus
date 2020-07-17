from app.crud.base import CRUDBase
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):
    pass


course = CRUDCourse(Course)
