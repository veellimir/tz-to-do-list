from core.models.users import User
from settings.database.repository import BaseDAO


class UsersDAO(BaseDAO):
    model = User
