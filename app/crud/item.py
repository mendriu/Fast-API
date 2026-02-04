from sqlalchemy.orm import Session

from app.models import Item
from app.schemas import ItemCreate


def get_items(db: Session, skip: int = 0, limit: int = 100) -> list[Item]:
    return db.query(Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Item | None:
    return db.query(Item).filter(Item.id == item_id).first()


def create_item(db: Session, item: ItemCreate) -> Item:
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: ItemCreate) -> Item | None:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return None
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int) -> bool:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True
