from sqlalchemy import Column, String, Text , Integer ,TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

Base = declarative_base()

class UserCreateBlog(Base):
    __tablename__ = "UserCreateBlog"
    Id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String)
    blog = Column(Text)
    CreateDateAndTime = Column(
        TIMESTAMP,
        default=datetime.utcnow
    )

