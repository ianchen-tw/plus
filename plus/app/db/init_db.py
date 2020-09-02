from sqlalchemy.orm import Session

from app import crud, schemas
from app.core import timetable_nctu
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def ensure_nctu_timeslots_exist(db: Session):
    """ Timeslots are prepolulate when app starts up
    """
    for day in range(1, 8):
        for code in timetable_nctu.get_valid_codes():
            ts = timetable_nctu.gen_timeslot(code=code, weekday_int=day)
            dic = ts._asdict()
            existing = crud.course_timeslot.find_timeslot(
                db=db, timeslot=schemas.CourseTimeslotCreate(**dic)
            )
            if not existing:
                crud.course_timeslot.create(
                    db=db, obj_in=schemas.CourseTimeslotCreate(**dic)
                )


def init_db(db: Session, use_fakedata=True) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    from app.db.session import engine

    base.Base.metadata.create_all(bind=engine)
    # Warning: Runnning tests would flush out the data created here entirely
    if use_fakedata:
        base.Base.metadata.drop_all(bind=engine)
        base.Base.metadata.create_all(bind=engine)

    # We need to makesure basic timeslots exist in our database before create
    ensure_nctu_timeslots_exist(db)

    # # Create Superuser
    # user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPERUSER,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         is_superuser=True,
    #     )
    #     user = crud.user.create(db, obj_in=user_in)  # noqa: F841
