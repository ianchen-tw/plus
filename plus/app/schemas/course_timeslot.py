from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.models.course_timeslot import TimeSlotKind, WeekDay


# Shared properties
class CourseTimeslotBase(BaseModel):
    code: str = Field(example="A")
    timespan: str = Field(example="7:00-7:50")
    weekday: WeekDay = Field(example=WeekDay.Fri)
    kind: TimeSlotKind = Field(example=TimeSlotKind.nctu)
    location: str = Field(example="EC022")


class CourseTimeslotCreate(CourseTimeslotBase):
    """Class for validating create CourseTimeslot request"""


class CourseTimeslotUpdate(CourseTimeslotBase):
    """Class for validating update CourseTimeslot request"""

    code: Optional[str] = Field(None, example="B")
    timespan: Optional[int] = Field(None, example="8:00-8:50")
    weekday: Optional[WeekDay] = Field(None, example=WeekDay.Tue)
    kind: Optional[TimeSlotKind] = Field(None, example=TimeSlotKind.nctu)
    location: str = Field(None, example="EC022")


# Propeties to return to client
class CourseTimeslot(CourseTimeslotBase):
    class Config:
        orm_mode = True

    @classmethod
    def get_example(cls):
        # There's a bug in FastAPI for rendering nested example by default Field() method,
        # so we defined our exmaple method and get it outside
        return CourseTimeslot(
            code="C",
            timespan="10:00-10:50",
            weekday=WeekDay.Wed,
            kind=TimeSlotKind.nctu,
            location="ED202",
        )


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
