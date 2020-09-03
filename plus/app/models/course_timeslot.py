import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
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


class TimeSlotKind(enum.Enum):
    """ Which kind of this timeslot used to represent data"""

    nctu = "nctu"


class CourseTimeslot(Base):
    """
    This represent a single slot in the timetable.
    e.g. 2AB would results in 2 rows in this table:

      CourseTimeslot( code='A', weekday='Tue', timespan='8:00-8:50', kind='nctu')
      and
      CourseTimeslot( code='B', weekday='Tue', timespan='9:00-8:50', kind='nctu')
    """

    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    # general info
    code = Column(String, nullable=False)  # may duplicate
    timespan = Column(String, nullable=False)  # e.g. "8:00-8:50"
    weekday = Column(Enum(WeekDay), nullable=False)
    kind = Column(Enum(TimeSlotKind), nullable=False)

    # Relation
    # A CourseTimeslot belongs to a single course
    course_id = Column(Integer, ForeignKey("course.id", ondelete="CASCADE"))
    course = relationship("Course", back_populates="timeslots")
