from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    connect_args={"check_same_thread": False},
)

# This obeject is used to create sessions to connect to database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
