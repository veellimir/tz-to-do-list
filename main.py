from fastapi import FastAPI
from api_v1 import router as api_router


app = FastAPI()
app.include_router(api_router)
