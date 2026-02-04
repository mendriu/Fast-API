from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[ItemResponse])
async def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id, item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    if not crud.delete_item(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
