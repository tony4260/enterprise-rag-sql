from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    access_level = Column(String, nullable=False)

    version = Column(Integer, default=1)

    created_at = Column(DateTime, default=datetime.utcnow)