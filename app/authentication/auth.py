# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from settings.env_config import (
    CONFIG__SECRET_KEY,
    CONFIG__ALGORITHM,
    CONFIG__ACCESS_TOKEN_EXPIRE_MINUTES,
    CONFIG__REFRESH_TOKEN_EXPIRE_DAYS
)

SECRET_KEY = CONFIG__SECRET_KEY
ALGORITHM = CONFIG__ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = CONFIG__ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=CONFIG__REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
