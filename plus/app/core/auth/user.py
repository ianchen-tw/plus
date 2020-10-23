from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import crud


class UserHandler:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_user_if_not_exist(self, student_id: str, email: EmailStr):
        user = crud.user.find_by_student_id(self.db, student_id=student_id)
        if user is None:
            user = crud.user.create(
                db=self.db, obj_in={"student_id": student_id, "email": email},
            )
        return user
