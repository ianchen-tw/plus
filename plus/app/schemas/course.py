from datetime import datetime
from typing import List

from pydantic import BaseModel

from .course_timeslot import CourseTimeslotInDB


# Shared properties
class CourseBase(BaseModel):
    permanent_id: str
    credit: int
    hours: int
    semester: str
    teacher: str

    class Config:
        schema_extra = {
            "example": {
                "permanent_id": "DCP2312",
                "credit": 4,
                "hours": 3,
                "semester": "108A",
                "teacher": "張書銘",
            }
        }


class CourseCreateAPI(CourseBase):
    """Class for validating create Course request"""

    timeslot_ids: List[int]

    class Config:
        schema_extra = {
            "example": {
                "permanent_id": "DCP2312",
                "credit": 4,
                "hours": 3,
                "semester": "108A",
                "teacher": "張書銘",
                "timeslot_ids": [2, 5, 19],
            }
        }


class CourseCreate(CourseBase):
    """Class for validating create Course request"""


class CourseUpdate(CourseBase):
    """Class for update Course """


class CourseUpdateAPI(CourseBase):
    """Class for validating update Course request"""

    timeslot_ids: List[int]


# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class Course(CourseInDBBase):
    timeslots: List[CourseTimeslotInDB]


# Properties stored in DB
class CourseInDB(CourseInDBBase):
    pass
