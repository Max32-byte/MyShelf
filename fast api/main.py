from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (frontend toegang)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== In-memory data =====
books = {
    "978-0-123456-78-9": {
        "title": "Python Basics",
        "author": "John Doe",
        "available": True,
        "borrowed_by": None,
    },
    "978-0-987654-32-1": {
        "title": "FastAPI Guide",
        "author": "Jane Smith",
        "available": True,
        "borrowed_by": None,
    },
}

members = {
    1: {
        "name": "Alice",
        "email": "alice@example.com",
        "borrowed_books": [],
    },
    2: {
        "name": "Bob",
        "email": "bob@example.com",
        "borrowed_books": [],
    },
}

# ===== Models =====
class Book(BaseModel):
    title: str
    author: str
    available: bool = True
    borrowed_by: Optional[int] = None


class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    available: Optional[bool] = None


class Member(BaseModel):
    name: str
    email: str
    borrowed_books: List[str] = []


class UpdateMember(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


# ===== Routes =====
@app.get("/")
def index():
    return {"message": "Welkom bij de Bibliotheek API"}


# --- Books ---
@app.get("/books")
def get_all_books():
    return [{"isbn": isbn, **info} for isbn, info in books.items()]


@app.get("/books/{isbn}")
def get_book(isbn: str):
    if isbn not in books:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    return {"isbn": isbn, **books[isbn]}


@app.post("/books/{isbn}")
def add_book(isbn: str, book: Book):
    if isbn in books:
        raise HTTPException(status_code=400, detail="Book exists")
    books[isbn] = book.dict()
    return {"isbn": isbn, **books[isbn]}


@app.put("/books/{isbn}")
def update_book(isbn: str, book: UpdateBook):
    if isbn not in books:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")

    if book.title is not None:
        books[isbn]["title"] = book.title
    if book.author is not None:
        books[isbn]["author"] = book.author
    if book.available is not None:
        books[isbn]["available"] = book.available

    return {"isbn": isbn, **books[isbn]}


@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    if isbn not in books:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    del books[isbn]
    return {"message": "Boek verwijderd"}


# --- Members ---
@app.get("/members")
def get_all_members():
    return [{"id": member_id, **info} for member_id, info in members.items()]


@app.post("/members/{member_id}")
def add_member(member_id: int, member: Member):
    if member_id in members:
        raise HTTPException(status_code=400, detail="Member exists")
    members[member_id] = member.dict()
    return {"id": member_id, **members[member_id]}


# --- Borrow / Return ---
@app.post("/borrow/{isbn}/{member_id}")
def borrow_book(isbn: str, member_id: int):
    if isbn not in books:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    if member_id not in members:
        raise HTTPException(status_code=404, detail="Lid niet gevonden")

    book = books[isbn]
    member = members[member_id]

    if not book["available"]:
        raise HTTPException(status_code=400, detail="Boek is al uitgeleend")

    book["available"] = False
    book["borrowed_by"] = member_id
    member["borrowed_books"].append(isbn)

    return {
        "message": "Boek succesvol geleend",
        "isbn": isbn,
        "member_id": member_id,
    }


@app.post("/return/{isbn}")
def return_book(isbn: str):
    if isbn not in books:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")

    book = books[isbn]

    if book["available"]:
        raise HTTPException(status_code=400, detail="Boek is niet uitgeleend")

    member_id = book["borrowed_by"]
    member = members.get(member_id)

    if member and isbn in member["borrowed_books"]:
        member["borrowed_books"].remove(isbn)

    book["available"] = True
    book["borrowed_by"] = None

    return {"message": "Boek succesvol teruggebracht"}
