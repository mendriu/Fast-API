from fastapi import FastAPI

from app.database import Base, engine
from app.routers.items import router as items_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Project", version="1.0.0")

app.include_router(items_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
