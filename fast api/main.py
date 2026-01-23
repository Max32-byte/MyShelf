from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
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
    "9780140328721": {
        "isbn_10": "0140328726",
        "isbn_13": "9780140328721",
        "openlibrary_work_id": "OL45804W",
        "openlibrary_edition_id": "OL7353617M",
        "title": "Matilda",
        "subtitle": None,
        "authors": ["Roald Dahl"],
        "publish_date": "1988",
        "publishers": ["Puffin"],
        "languages": ["en"],
        "subjects": ["Children", "Fiction", "Magic"],
      "covers": {
    "source": "openlibrary",
    "recommended": "large",
    "urls": {
        "small": "https://covers.openlibrary.org/b/isbn/9780140328721-S.jpg",
        "medium": "https://covers.openlibrary.org/b/isbn/9780140328721-M.jpg",
        "large": "https://covers.openlibrary.org/b/isbn/9780140328721-L.jpg",
    },
},
        "description": "A brilliant girl with extraordinary powers challenges cruel adults.",
        "available": True,
        "borrowed_by": None,
    },

    "9780061120084": {
        "isbn_10": "0061120081",
        "isbn_13": "9780061120084",
        "openlibrary_work_id": "OL82563W",
        "openlibrary_edition_id": "OL22572640M",
        "title": "To Kill a Mockingbird",
        "subtitle": None,
        "authors": ["Harper Lee"],
        "publish_date": "1960",
        "publishers": ["J.B. Lippincott & Co."],
        "languages": ["en"],
        "subjects": ["Fiction", "Race", "Justice"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/8225261-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/8225261-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/8225261-L.jpg",
        },
        "description": "A story of racial injustice and moral growth in the Deep South.",
        "available": True,
        "borrowed_by": None,
    },

    "9780451524935": {
        "isbn_10": "0451524934",
        "isbn_13": "9780451524935",
        "openlibrary_work_id": "OL73403W",
        "openlibrary_edition_id": "OL26476014M",
        "title": "1984",
        "subtitle": None,
        "authors": ["George Orwell"],
        "publish_date": "1949",
        "publishers": ["Secker & Warburg"],
        "languages": ["en"],
        "subjects": ["Dystopia", "Politics", "Surveillance"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/7222246-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/7222246-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/7222246-L.jpg",
        },
        "description": "A dystopian novel about total surveillance and loss of freedom.",
        "available": True,
        "borrowed_by": None,
    },

    "9780743273565": {
        "isbn_10": "0743273567",
        "isbn_13": "9780743273565",
        "openlibrary_work_id": "OL27627W",
        "openlibrary_edition_id": "OL24367537M",
        "title": "The Great Gatsby",
        "subtitle": None,
        "authors": ["F. Scott Fitzgerald"],
        "publish_date": "1925",
        "publishers": ["Charles Scribner's Sons"],
        "languages": ["en"],
        "subjects": ["Classic", "Wealth", "American Dream"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/589084-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/589084-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/589084-L.jpg",
        },
        "description": "A tragic story of obsession, wealth, and lost dreams.",
        "available": True,
        "borrowed_by": None,
    },

    "9780307474278": {
        "isbn_10": "0307474275",
        "isbn_13": "9780307474278",
        "openlibrary_work_id": "OL15447063W",
        "openlibrary_edition_id": "OL24367588M",
        "title": "The Road",
        "subtitle": None,
        "authors": ["Cormac McCarthy"],
        "publish_date": "2006",
        "publishers": ["Knopf"],
        "languages": ["en"],
        "subjects": ["Post-apocalyptic", "Survival"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/7222161-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/7222161-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/7222161-L.jpg",
        },
        "description": "A father and son journey through a devastated world.",
        "available": True,
        "borrowed_by": None,
    },

    "9780135166307": {
        "isbn_10": "0135166306",
        "isbn_13": "9780135166307",
        "openlibrary_work_id": "OL27841240W",
        "openlibrary_edition_id": "OL38630275M",
        "title": "Clean Code",
        "subtitle": "A Handbook of Agile Software Craftsmanship",
        "authors": ["Robert C. Martin"],
        "publish_date": "2008",
        "publishers": ["Prentice Hall"],
        "languages": ["en"],
        "subjects": ["Programming", "Software Engineering"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/9641981-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/9641981-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/9641981-L.jpg",
        },
        "description": "Best practices for writing clean, maintainable code.",
        "available": True,
        "borrowed_by": None,
    },

    "9781491950357": {
        "isbn_10": "1491950358",
        "isbn_13": "9781491950357",
        "openlibrary_work_id": "OL17341065W",
        "openlibrary_edition_id": "OL26431241M",
        "title": "Designing Data-Intensive Applications",
        "subtitle": None,
        "authors": ["Martin Kleppmann"],
        "publish_date": "2017",
        "publishers": ["O'Reilly Media"],
        "languages": ["en"],
        "subjects": ["Databases", "Distributed Systems"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/8369256-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/8369256-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/8369256-L.jpg",
        },
        "description": "Foundations of scalable and reliable data systems.",
        "available": True,
        "borrowed_by": None,
    },

    "9780132350884": {
        "isbn_10": "0132350882",
        "isbn_13": "9780132350884",
        "openlibrary_work_id": "OL262758W",
        "openlibrary_edition_id": "OL24289263M",
        "title": "Clean Architecture",
        "subtitle": None,
        "authors": ["Robert C. Martin"],
        "publish_date": "2017",
        "publishers": ["Prentice Hall"],
        "languages": ["en"],
        "subjects": ["Software Architecture"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/8231996-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/8231996-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/8231996-L.jpg",
        },
        "description": "Timeless principles for building maintainable software.",
        "available": True,
        "borrowed_by": None,
    },

    "9780596007126": {
        "isbn_10": "0596007124",
        "isbn_13": "9780596007126",
        "openlibrary_work_id": "OL57435W",
        "openlibrary_edition_id": "OL18371865M",
        "title": "Head First Design Patterns",
        "subtitle": None,
        "authors": ["Eric Freeman", "Elisabeth Robson"],
        "publish_date": "2004",
        "publishers": ["O'Reilly Media"],
        "languages": ["en"],
        "subjects": ["Design Patterns", "Programming"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/240726-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/240726-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/240726-L.jpg",
        },
        "description": "A visually rich guide to design patterns.",
        "available": True,
        "borrowed_by": None,
    },

    "9780262033848": {
        "isbn_10": "0262033844",
        "isbn_13": "9780262033848",
        "openlibrary_work_id": "OL18758004W",
        "openlibrary_edition_id": "OL26402760M",
        "title": "Introduction to Algorithms",
        "subtitle": None,
        "authors": ["Thomas H. Cormen"],
        "publish_date": "2009",
        "publishers": ["MIT Press"],
        "languages": ["en"],
        "subjects": ["Algorithms", "Computer Science"],
        "covers": {
            "small": "https://covers.openlibrary.org/b/id/1351822-S.jpg",
            "medium": "https://covers.openlibrary.org/b/id/1351822-M.jpg",
            "large": "https://covers.openlibrary.org/b/id/1351822-L.jpg",
        },
        "description": "The definitive textbook on algorithms.",
        "available": True,
        "borrowed_by": None,
    },
}

members = {
    1: {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "borrowed_books": [],
    },
    2: {
        "name": "Bob Smith",
        "email": "bob.smith@example.com",
        "borrowed_books": [],
    },
    3: {
        "name": "Charlie Brown",
        "email": "charlie.brown@example.com",
        "borrowed_books": [],
    },
    4: {
        "name": "Diana Evans",
        "email": "diana.evans@example.com",
        "borrowed_books": [],
    },
    5: {
        "name": "Ethan Miller",
        "email": "ethan.miller@example.com",
        "borrowed_books": [],
    },
    6: {
        "name": "Fiona Clark",
        "email": "fiona.clark@example.com",
        "borrowed_books": [],
    },
    7: {
        "name": "George Wilson",
        "email": "george.wilson@example.com",
        "borrowed_books": [],
    },
    8: {
        "name": "Hannah Lee",
        "email": "hannah.lee@example.com",
        "borrowed_books": [],
    },
    9: {
        "name": "Ian Walker",
        "email": "ian.walker@example.com",
        "borrowed_books": [],
    },
    10: {
        "name": "Julia Martinez",
        "email": "julia.martinez@example.com",
        "borrowed_books": [],
    },
    11: {
        "name": "Kevin Anderson",
        "email": "kevin.anderson@example.com",
        "borrowed_books": [],
    },
    12: {
        "name": "Laura Thompson",
        "email": "laura.thompson@example.com",
        "borrowed_books": [],
    },
}


# ===== Models =====
class Book(BaseModel):
    # ---- Identifiers ----
    isbn_10: Optional[str] = None
    isbn_13: Optional[str] = None
    openlibrary_work_id: Optional[str] = None
    openlibrary_edition_id: Optional[str] = None

    # ---- Core metadata ----
    title: str
    subtitle: Optional[str] = None
    authors: List[str]
    publish_date: Optional[str] = None
    publishers: List[str] = []
    languages: List[str] = []
    subjects: List[str] = []

    # ---- Covers ----

    covers: Optional[Dict[str, str]] = None
    # example:
    # {
    #   "small": "...-S.jpg",
    #   "medium": "...-M.jpg",
    #   "large": "...-L.jpg"
    # }

    # ---- Description ----
    description: Optional[str] = None

    # ---- Local library state ----
    available: bool = True
    borrowed_by: Optional[int] = None


class UpdateBook(BaseModel):
    # ---- Core metadata ----
    title: Optional[str] = None
    subtitle: Optional[str] = None
    authors: Optional[List[str]] = None
    publish_date: Optional[str] = None
    publishers: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    subjects: Optional[List[str]] = None
    description: Optional[str] = None

    # ---- Covers ----
    covers: Optional[Dict[str, str]] = None

    # ---- Local state ----
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
