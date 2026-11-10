from fastapi import FastAPI

app = FastAPI(title="Book API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "year": 1962},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


@app.get("/books")
def list_books():
    return books
