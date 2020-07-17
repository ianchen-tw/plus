from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class CourseBase(BaseModel):
    permanent_id: str
    credit: int
    hours: int
    semester: str
    teacher: str


class CourseCreate(CourseBase):
    """Class for validating create Course request"""


class CourseUpdate(CourseBase):
    """Class for validating update Course request"""

    permanent_id: Optional[str] = None
    creidt: Optional[int] = None
    hours: Optional[int] = None
    semester: Optional[str] = None
    teacher: Optional[str] = None


# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    id: int
    permanent_id: str
    credit: int
    hours: int
    semester: str
    teacher: str

    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class Course(CourseInDBBase):
    pass


# Properties stored in DB
class CourseInDB(CourseInDBBase):
    pass
