# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .library import Book as LibBook, Library

app = FastAPI(title="Library API (in-memory)")

# Pydantic schemas
class BookIn(BaseModel):
    number: int
    name: str
    price: float
    pages: int
    author: str

class BookOut(BookIn):
    is_sold: bool

# Instancia global en memoria
_initial = [
    LibBook(1, "peppa pig", 100, 50, "juan gabriel", False),
    LibBook(2, "francisco del sesus", 100, 60, "juan gabriel", False),
]
lib = Library(_initial)

@app.get("/books", response_model=List[BookOut])
def list_books():
    return [BookOut(**b.__dict__) for b in lib.getList()]

@app.post("/books", status_code=201, response_model=BookOut)
def create_book(book: BookIn):
    new = LibBook(**book.dict(), is_sold=False)
    lib.addNewBook(new)
    return BookOut(**new.__dict__)

@app.delete("/books/{name}", status_code=204)
def delete_book(name: str):
    before = len(lib.getList())
    lib.deleteBook(name)
    if len(lib.getList()) == before:
        raise HTTPException(404, detail="Book not found")

@app.patch("/books/{name}/pages", response_model=BookOut)
def add_pages(name: str, pages: int):
    lib.addPagesBook(name, pages)
    for b in lib.getList():
        if b.name == name:
            return BookOut(**b.__dict__)
    raise HTTPException(404, detail="Book not found")

@app.patch("/books/{name}/sell", response_model=BookOut)
def sell_book(name: str):
    lib.sellBook(name)
    for b in lib.getList():
        if b.name == name:
            return BookOut(**b.__dict__)
    raise HTTPException(404, detail="Book not found")
