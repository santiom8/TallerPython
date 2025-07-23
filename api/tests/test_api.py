# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from app.library import Book as LibBook        # <-- Importa tu clase interna
from app.main import app, lib

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_library():
    # Cada test parte de la librería inicial
    lib.__init__([
        LibBook(1, "peppa pig", 100, 50, "juan gabriel", False),
        LibBook(2, "francisco del sesus", 100, 60, "juan gabriel", False),
    ])
    yield

def test_list_books():
    r = client.get("/books")
    assert r.status_code == 200
    assert len(r.json()) == 2

def test_create_book_and_list():
    payload = {"number":3,"name":"X","price":10,"pages":5,"author":"Y"}
    r = client.post("/books", json=payload)
    assert r.status_code == 201
    assert r.json()["name"] == "X"
    r2 = client.get("/books")
    assert any(b["name"]=="X" for b in r2.json())

def test_delete_book():
    r = client.delete("/books/peppa pig")
    assert r.status_code == 204
    r2 = client.get("/books")
    assert all(b["name"]!="peppa pig" for b in r2.json())

def test_add_pages():
    r = client.patch("/books/francisco del sesus/pages", params={"pages":10})
    assert r.status_code == 200
    assert r.json()["pages"] == 70

def test_sell_book():
    r = client.patch("/books/francisco del sesus/sell")
    assert r.status_code == 200
    assert r.json()["is_sold"] is True
