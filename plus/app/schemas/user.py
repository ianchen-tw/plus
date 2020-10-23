from datetime import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    student_id = str
    name = str
    email = EmailStr
    admission_year = int
    role = int
    last_sign_in_at = datetime
    last_sign_in_ip = str
    agree_to_share_course_table = bool


class UserCreate(UserBase):
    """Class for validating create User request"""

    student_id = str
    email = EmailStr


class UserUpdate(UserBase):
    """Class for validating update User request"""


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True


# Propeties to return to client
class User(UserInDBBase):
    pass


# Properties stored in DB
class UserInDB(UserInDBBase):
    pass
