from sqlalchemy import Column, Integer, String, Boolean, Float, Enum as AlEnum, DateTime
from app.database import Base
from enum import Enum
from typing import Optional
from datetime import timezone,datetime
import uuid

# Define the CronJob model for SQLAlchemy
class CronJob(Base):
    __tablename__ = 'cron_jobs'  # Ensure the table name is specified
    id = Column(Integer, primary_key=True, autoincrement=True)  # No need for autoincrement with String
    cron_expression = Column(String)
    function = Column(String)

# Define the User model for SQLAlchemy
class UserStatus(str,Enum):
    ACTIVE = "active"

class UserRole(str,Enum):
    USER = "user"

class User(Base):
    __tablename__ = 'users'  # Ensure the table name is specified
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))  # No need for autoincrement with String
    name = Column(String)
    discriminator = Column(AlEnum(UserRole))
    avatar = Column(String, default="")
    bot = Column(Boolean)
    display_name = Column(String)
    joined_at = Column(DateTime(True), default=datetime.now(timezone.utc))
    status = Column(AlEnum(UserStatus))
    password = Column(String)

# Define the Channel model for SQLAlchemy
class Channel(Base):
    __tablename__ = 'channels'  # Ensure the table name is specified
    id = Column(String, primary_key=True, default=str(uuid.uuid4))  # No need for autoincrement with String
    name = Column(String)
    type = Column(Integer)
    created_at = Column(Float)
