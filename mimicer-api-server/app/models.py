from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base
from typing import Optional

# Define the CronJob model for SQLAlchemy
class CronJob(Base):
    __tablename__ = 'cron_jobs'  # Ensure the table name is specified
    id = Column(Integer, primary_key=True, autoincrement=True)  # No need for autoincrement with String
    cron_expression = Column(String)
    function = Column(String)

# Define the User model for SQLAlchemy
class User(Base):
    __tablename__ = 'users'  # Ensure the table name is specified
    id = Column(String, primary_key=True)  # No need for autoincrement with String
    name = Column(String)
    discriminator = Column(String)
    avatar = Column(String)
    bot = Column(Boolean)
    created_at = Column(Float)
    display_name = Column(String)
    joined_at = Column(Float)
    status = Column(String)

# Define the Channel model for SQLAlchemy
class Channel(Base):
    __tablename__ = 'channels'  # Ensure the table name is specified
    id = Column(String, primary_key=True)  # No need for autoincrement with String
    name = Column(String)
    type = Column(Integer)
    created_at = Column(Float)