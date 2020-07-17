from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.db.base_class import Base


class Course(Base):
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DateTime, nullable=False, default=func.now())
    update_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    # general info
    permanent_id = Column(String)
    credit = Column(Integer)
    hours = Column(Integer)  # do we need this?
    semester = Column(String)
    teacher = Column(String)
