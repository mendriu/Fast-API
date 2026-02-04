from fastapi import APIRouter, HTTPException

from app.schemas import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

# Tymczasowa "baza danych" w pamięci
fake_db: dict[int, dict] = {}
counter = 0


@router.get("/", response_model=list[ItemResponse])
async def list_items():
    return list(fake_db.values())


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate):
    global counter
    counter += 1
    item_dict = {"id": counter, **item.model_dump()}
    fake_db[counter] = item_dict
    return item_dict


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item_dict = {"id": item_id, **item.model_dump()}
    fake_db[item_id] = item_dict
    return item_dict


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
