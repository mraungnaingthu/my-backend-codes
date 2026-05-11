from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

fake_items_db = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be a positive number")
    fake_items_db.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def read_items():
    return fake_items_db

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    if updated_item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be a positive number")
    fake_items_db[item_id] = updated_item
    return updated_item

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = fake_items_db.pop(item_id)
    return deleted_item