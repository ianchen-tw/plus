from typing import Optional
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class CollegeBase(BaseModel):
    name: str
    code: str


class CollegeCreate(CollegeBase):
    """Class for validating create college request"""

    pass


class CollegeUpdate(CollegeBase):
    """Class for validating update college request"""

    name: Optional[str] = None
    code: Optional[str] = None


# Properties shared by models stored in DB
class CollegeInDBBase(CollegeBase):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class College(CollegeInDBBase):
    pass


# Properties stored in DB
class CollegeInDB(CollegeInDBBase):
    pass
