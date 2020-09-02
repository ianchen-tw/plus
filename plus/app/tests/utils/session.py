from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.init_db import init_db

# We use the same database simply for easier developing
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True,)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initalize the database whenever we restart the server
init_db(TestingSessionLocal())
