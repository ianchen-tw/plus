from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .course_timeslot import CourseTimeslot
from .timeslot_exp import TimeSlotExp


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


# TODO: verify the usage of this schema
class CourseCreate(CourseBase):
    """Class for validating create Course request"""


class CourseUpdate(CourseBase):
    """Class for update Course """

    permanent_id: Optional[str] = None
    credit: Optional[int] = None
    hours: Optional[int] = None
    semester: Optional[str] = None
    teacher: Optional[str] = None


class CourseAPI(CourseBase):
    """ Course schema expose to API level"""

    timeslots: TimeSlotExp

    class Config:
        schema_extra = {
            "example": {
                "permanent_id": "DCP2312",
                "credit": 4,
                "hours": 3,
                "semester": "108A",
                "teacher": "張書銘",
                "timeslots": {"kind": "nctu", "value": "2AB5CD"},
            }
        }


class CourseCreateAPI(CourseAPI):
    """Class for validating create Course request"""


class CourseUpdateAPI(CourseAPI):
    """Class for validating update Course request"""

    permanent_id: Optional[str] = None
    credit: Optional[int] = None
    hours: Optional[int] = None
    semester: Optional[str] = None
    teacher: Optional[str] = None
    timeslots: Optional[TimeSlotExp] = None


# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class Course(CourseInDBBase):
    timeslots: List[CourseTimeslot]


# Properties stored in DB
class CourseInDB(CourseInDBBase):
    pass


class CourseWithTimeslotsInDB(CourseInDBBase):
    timeslots: List[CourseTimeslot]
