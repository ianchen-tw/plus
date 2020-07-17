import enum

from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.sql import func

from app.db.base_class import Base


class WeekDay(enum.Enum):
    Mon = "Mon"
    Tue = "Tue"
    Wed = "Wed"
    Thr = "Thr"
    Fri = "Fri"
    Sat = "Sat"
    Sun = "Sun"


class CourseTimeslot(Base):
    """
    This represent a single slot in the timetable.
    e.g. 2AB would results in 2 rows in this table:

      CourseTimeslot( codeName='A', weekday='Tue')
      and
      CourseTimeslot( codeName='B', weekday='Tue')
    """

    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    # general info
    code_name = Column(String, nullable=False)  # may duplicate
    description = Column(String, nullable=False)  # e.g. "8:00-8:50"
    weekday = Column(Enum(WeekDay), nullable=False)
