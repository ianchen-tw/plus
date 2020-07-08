from app.crud.base import CRUDBase
from app.models.college import College
from app.schemas.college import CollegeCreate, CollegeUpdate


class CRUDCollege(CRUDBase[College, CollegeCreate, CollegeUpdate]):
    pass
    # def create(self, db: Session, *, obj_in: CollegeCreate ) -> College:
    #     db_obj = CollegeInDB(**obj_in.dict())


college = CRUDCollege(College)
