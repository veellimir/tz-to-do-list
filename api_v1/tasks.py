from fastapi import APIRouter, Depends, HTTPException
from . import models, schemas, crud, auth
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()


# CRUD операции для задач
@router.post("/tasks")
async def create_task(task: schemas.TaskCreate, token: str = Depends(oauth2_scheme)):
    # Создание задачи
    pass


@router.get("/tasks")
async def read_tasks(status: str = None, token: str = Depends(oauth2_scheme)):
    # Получение задач с фильтром
    pass
