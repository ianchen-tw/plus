from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey, Table
from sqlalchemy.sql import func

from app.db.base_class import Base

course_timeslot_relation = Table(
    "course_timeslot_relation",
    Base.metadata,
    Column("course_id", Integer, ForeignKey("course.id")),
    Column("cours_timeslot_id", Integer, ForeignKey("coursetimeslot.id")),
)


class Course(Base):
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    timeslots = relationship(
        "CourseTimeslot", secondary=course_timeslot_relation, back_populates="courses"
    )

    # general info
    permanent_id = Column(String)
    credit = Column(Integer)
    hours = Column(Integer)  # do we need this?
    semester = Column(String)
    teacher = Column(String)
