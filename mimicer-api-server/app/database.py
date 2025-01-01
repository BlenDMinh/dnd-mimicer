import logging
from typing import Annotated
from fastapi import Depends
import env
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

logger = logging.getLogger(__name__)

# Define the database connection
engine = create_engine(env.DB_URL, echo=True)
logger.info(f"Database URL: {env.DB_URL}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]
