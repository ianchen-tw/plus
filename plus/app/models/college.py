from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.func import current_timestamp
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class College(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=current_timestamp())
