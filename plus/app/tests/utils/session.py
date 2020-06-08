from typing import Optional, Any, Dict

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

from app.db.base import Base


# We use the same database simply for easier developing
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True,)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# clear the database whenever we restart the server
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
