from fastapi import APIRouter, Depends, HTTPException
from . import models, schemas, crud, auth
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/auth/register")
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Реализовать логику
    pass


@router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Логика авторизации и генерации токенов
    pass


@router.post("/auth/refresh")
async def refresh_token(token: str, db: Session = Depends(get_db)):
    # Логика обновления access-токена
    pass
