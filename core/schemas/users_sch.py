from pydantic import BaseModel


class UserBaseSchem(BaseModel):
    username: str


class UserCreateSchem(UserBaseSchem):
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
