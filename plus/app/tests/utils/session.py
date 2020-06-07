from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base

# TODO: fix this
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# clear the database whenever we restart the server
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
