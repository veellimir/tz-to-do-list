from pydantic import BaseModel


class TaskBaseSchem(BaseModel):
    title: str
    description: str
    status: str


class TaskCreateSchem(TaskBaseSchem):
    pass


class TaskSchem(TaskBaseSchem):
    id: int
    user_id: int

    class Config:
        orm_mode = True
