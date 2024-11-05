from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from settings.database.base import Base
from core.models.mixins_models import IdIntPkMixin


class Task(IdIntPkMixin, Base):
    __tablename__ = "tasks"

    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, default="in_progress")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")
