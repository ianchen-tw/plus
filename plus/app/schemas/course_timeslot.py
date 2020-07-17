from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.course_timeslot import WeekDay


# Shared properties
class CourseTimeslotBase(BaseModel):
    code_name: str
    description: str
    weekday: WeekDay


class CourseTimeslotCreate(CourseTimeslotBase):
    """Class for validating create CourseTimeslot request"""


class CourseTimeslotUpdate(CourseTimeslotBase):
    """Class for validating update CourseTimeslot request"""

    code_name: Optional[str] = None
    description: Optional[int] = None
    weekday: Optional[WeekDay] = None


# Properties shared by models stored in DB
class CourseTimeslotInDBBase(CourseTimeslotBase):
    id: int
    code_name: str
    description: str
    weekday: WeekDay

    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class CourseTimeslot(CourseTimeslotInDBBase):
    pass


# Properties stored in DB
class CourseTimeslotInDB(CourseTimeslotInDBBase):
    pass
