from typing import Optional
from datetime import datetime
from pydantic import BaseModel

# Shared properties
class CollegeBase(BaseModel):
    name: str
    code: str


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
