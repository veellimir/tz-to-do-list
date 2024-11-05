from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from settings.env_config import (
    CONFIG__SECRET_KEY,
    CONFIG__ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS
)
from .dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, CONFIG__SECRET_KEY, algorithm=CONFIG__ALGORITHM)


def create_refresh_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, CONFIG__SECRET_KEY, algorithm=CONFIG__ALGORITHM)


async def authenticated_user(username: str, password: str):
    user = await UsersDAO.find_one_or_none(username=username)

    if not user and verify_password(password, user.password):
        return None
    return user
