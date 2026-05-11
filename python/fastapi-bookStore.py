from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

books_db = []

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    books_db.append(book)
    return book

@app.get("/books/", response_model=list[Book])
async def read_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[index]
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")