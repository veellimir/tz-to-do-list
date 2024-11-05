from pydantic import BaseModel


class UserBaseSchem(BaseModel):
    username: str


class UserCreateSchem(UserBaseSchem):
    password: str
