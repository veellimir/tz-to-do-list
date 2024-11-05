from sqlalchemy import Column, Integer, String

from settings.database.base import Base
from core.models.mixins_models import IdIntPkMixin


class User(IdIntPkMixin, Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
