from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def find_by_student_id(self, db: Session, *, student_id) -> Optional[User]:
        return db.query(self.model).filter(self.model.student_id == student_id).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        obj_in_data = jsonable_encoder(obj_in)
        user = self.model(**obj_in_data)

        db.add(user)

        db.flush()
        db.commit()
        db.refresh(user)
        return user


user = CRUDUser(User)
