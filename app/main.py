from fastapi import FastAPI

from app.routers.items import router as items_router

app = FastAPI()

app.include_router(items_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}