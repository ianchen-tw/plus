from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from .course_timeslot import CourseTimeslot
from .timeslot_exp import TimeSlotExp


# Shared properties
class CourseBase(BaseModel):
    permanent_id: str = Field(example="DCP2312")
    credit: int = Field(example=4)
    hours: int = Field(example=3)
    semester: str = Field(example="108A")
    teacher: str = Field(example="張書銘")


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


class CourseCreateAPI(CourseAPI):
    """Class for validating create Course request"""


class CourseUpdateAPI(CourseAPI):
    """Class for validating update Course request"""

    permanent_id: Optional[str] = Field(None, example="DCP2312")
    credit: Optional[int] = Field(None, example=4)
    hours: Optional[int] = Field(None, example=3)
    semester: Optional[str] = Field(None, example="108A")
    teacher: Optional[str] = Field(None, example="張書銘")
    timeslots: Optional[TimeSlotExp] = None


# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    id: int = Field(example=3)
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
