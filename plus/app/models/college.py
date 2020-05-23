from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME

# from sqlalchemy.schema import FetchedValue
# from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class College(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    create_at = Column(DATETIME, nullable=False, default=datetime.now)
    update_at = Column(
        DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now
    )
