from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String(10), unique=True)
    name = Column(String(10))
    email = Column(String(321), nullable=False)
    admission_year = Column(Integer)
    role = Column(Integer, default=0)
    last_sign_in_at = Column(DateTime)
    last_sign_in_ip = Column(String(16))
    agree_to_share_course_table = Column(Boolean, nullable=False, default=False)

    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
