from sqlalchemy import Column, Float, Integer, String

from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=True)
