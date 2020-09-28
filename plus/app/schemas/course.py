from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from .course_timeslot import CourseTimeslot
from .timeslot_exp import TimeSlotExp


# Shared properties
class CourseBase(BaseModel):
    permanent_id: str = Field(example="DCP2312")
    credit: str = Field(example=4)
    hours: str = Field(example=3)
    semester: str = Field(example="108A")
    teacher: str = Field(example="張書銘")

    en_name: str = Field(example="Topics on Database Systems")
    zh_name: str = Field(example="資料庫系統專題")
    course_number: str = Field(example="5222")
    course_type: str = Field(example="選修")
    department_en: str = Field(example="Institute of Network Engineering")
    department_zh: str = Field(example="網路工程研究所")


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

    en_name: Optional[str] = Field(None, example="Topics on Database Systems")
    zh_name: Optional[str] = Field(None, example="資料庫系統專題")
    course_number: Optional[str] = Field(None, example="5222")
    course_type: Optional[str] = Field(None, example="選修")
    department_en: Optional[str] = Field(None, example="Institute of Network Engineering")
    department_zh: Optional[str] = Field(None, example="網路工程研究所")


class TimeExpLocation(BaseModel):
    time: TimeSlotExp = Field(example=TimeSlotExp.get_example())
    location: str = Field(example="EC012")


class CourseAPI(CourseBase):
    """ Course schema expose to API level"""

    # time_location is an abstract data, which would be converted to CourseTimeSlots internally.
    time_locations: List[TimeExpLocation]


class CourseCreateAPI(CourseAPI):
    """Class for validating create Course request"""


class CourseUpdateAPI(CourseAPI):
    """Class for validating update Course request"""

    permanent_id: Optional[str] = Field(None, example="DCP2312")
    credit: Optional[int] = Field(None, example=4)
    hours: Optional[int] = Field(None, example=3)
    semester: Optional[str] = Field(None, example="108A")
    teacher: Optional[str] = Field(None, example="張書銘")
    en_name: Optional[str] = Field(None, example="Topics on Database Systems")
    zh_name: Optional[str] = Field(None, example="資料庫系統專題")
    course_number: Optional[str] = Field(None, example="5222")
    course_type: Optional[str] = Field(None, example="選修")
    department_en: Optional[str] = Field(None, example="Institute of Network Engineering")
    department_zh: Optional[str] = Field(None, example="網路工程研究所")

    time_locations: Optional[List[TimeExpLocation]] = Field(None)


# Properties shared by models stored in DB
class CourseInDBBase(CourseBase):
    id: int = Field(example=3)
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class Course(CourseInDBBase):
    # timeslots: List[CourseTimeslot] = Field(example=CourseTimeslot.get_example())
    timeslots: List[CourseTimeslot]


# Properties stored in DB
class CourseInDB(CourseInDBBase):
    pass


class CourseWithTimeslotsInDB(CourseInDBBase):
    timeslots: List[CourseTimeslot]
