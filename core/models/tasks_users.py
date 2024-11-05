from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from settings.database.base import Base
from users import User


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, default="in_progress")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")
