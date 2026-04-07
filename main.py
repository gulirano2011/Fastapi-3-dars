from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title='Swagger',
    description='Bu fastapida yaratilgan',
    version='1.0.0'
)

items: List[Item] = []

class Item(BaseModel):
    name: str
    price: int
    description: str | None = None


@app.post(
    "/items",
    response_model=Item,
    summary="Yangi item qo'shish",
    tags=["items"]
)
async def create_item(item: Item):
    items.append(item)
    return item


@app.get(
    "/items",
    response_model=List[Item],
    summary="Barcha itemlarni olish",
    tags=["items"]
)
async def get_items():
    return items
