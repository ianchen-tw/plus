from datetime import datetime
from typing import Optional, Dict, Any, Type

from pydantic import BaseModel, Field

from app.models.course_timeslot import TimeSlotKind, WeekDay

from pprint import pprint

# Shared properties
class CourseTimeslotBase(BaseModel):
    code: str = Field(example="A")
    timespan: str = Field(example="7:00-7:50")
    weekday: WeekDay = Field(example="Fri")
    kind: TimeSlotKind = Field(example="nctu")


class CourseTimeslotCreate(CourseTimeslotBase):
    """Class for validating create CourseTimeslot request"""


class CourseTimeslotUpdate(CourseTimeslotBase):
    """Class for validating update CourseTimeslot request"""

    code: Optional[str] = None
    timespan: Optional[int] = None
    weekday: Optional[WeekDay] = None
    kind: Optional[TimeSlotKind] = None


# Propeties to return to client
class CourseTimeslot(CourseTimeslotBase):
    class Config:
        orm_mode = True


# Properties shared by models stored in DB
class CourseTimeslotInDBBase(CourseTimeslotBase):
    id: int = Field(example=1)
    course_id: int = Field(example=34)

    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Properties stored in DB
class CourseTimeslotInDB(CourseTimeslotInDBBase):
    pass
