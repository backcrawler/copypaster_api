import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import settings

if settings.DEBUG:
    DATABASE_URL = "sqlite:///../test.db"
    connect_args = {"check_same_thread": False}
else:
    DATABASE_URL = ""  # "postgresql://user:password@postgresserver/db"
    connect_args = {}  # not needed for non-sqlite DB


engine = create_engine(
    DATABASE_URL, connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



