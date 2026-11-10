import sqlite3
from pathlib import Path

from fastapi import FastAPI

app = FastAPI(title="SQLite Book API")
DATABASE_PATH = Path(__file__).with_name("books.db")


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
            """
        )
        connection.commit()


initialize_database()


@app.get("/")
def read_root():
    return {"message": "Welcome to the SQLite Book API"}
