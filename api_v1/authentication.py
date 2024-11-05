from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jwt import ExpiredSignatureError as JWTError

from app.authentication.dao import UsersDAO
from core.schemas.users_sch import UserCreateSchem, UserBaseSchem, Token
from app.authentication.auth import (
    get_hash_password,
    create_access_token,
    create_refresh_token,
    verify_password,
    authenticated_user
)

from app.authentication.exeptions import (
    UserAlreadyExistsException,
    IncorrectUsernameOrPswException
)

router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация пользователей"]
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/register", response_model=Token)
async def register(user_data: UserCreateSchem):
    existing_user = await UsersDAO.find_one_or_none(username=user_data.username)

    if existing_user:
        raise UserAlreadyExistsException

    password_hash = get_hash_password(user_data.password)
    await UsersDAO.add(username=user_data.username, password_hash=password_hash)

    access_token = create_access_token(data={"sub": user_data.username})
    refresh_token = create_refresh_token(data={"sub": user_data.username})
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.post("/login", response_model=Token)
async def login(response: Response, user_data: UserCreateSchem):
    user = await authenticated_user(user_data.username, user_data.password)
    if not user or not verify_password(user_data.password, user.password_hash):
        raise IncorrectUsernameOrPswException

    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
