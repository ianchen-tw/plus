from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.course_timeslot import TimeSlotKind, WeekDay


# Shared properties
class CourseTimeslotBase(BaseModel):
    code: str
    timespan: str
    weekday: WeekDay
    kind: TimeSlotKind

    class Config:
        schema_extra = {
            "example": {
                "code": "A",
                "timespan": "7:00-7:50",
                "weekday": "Fri",
                "kind": "nctu",
            }
        }


class CourseTimeslotCreate(CourseTimeslotBase):
    """Class for validating create CourseTimeslot request"""


class CourseTimeslotUpdate(CourseTimeslotBase):
    """Class for validating update CourseTimeslot request"""

    code: Optional[str] = None
    timespan: Optional[int] = None
    weekday: Optional[WeekDay] = None
    kind: Optional[TimeSlotKind] = None


# Properties shared by models stored in DB
class CourseTimeslotInDBBase(CourseTimeslotBase):
    id: int
    code: str
    timespan: str
    weekday: WeekDay
    kind: TimeSlotKind

    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class CourseTimeslot(CourseTimeslotBase):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 3,
                "code": "A",
                "timespan": "7:00-7:50",
                "weekday": "Fri",
                "kind": "nctu",
            },
        }


# Properties stored in DB
class CourseTimeslotInDB(CourseTimeslotInDBBase):
    pass
