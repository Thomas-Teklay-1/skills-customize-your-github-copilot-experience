# 📘 Assignment: Persisting API Data with SQLite

## 🎯 Objective

Extend a FastAPI book service so its data is stored in a local SQLite database instead of an in-memory list. You will practice database schema design, SQL queries, request validation, and connecting persistent data to REST endpoints.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Description

Use the provided starter file to create a SQLite database for the book service. Define a table that stores each book's ID, title, author, and publication year.

#### Requirements

Completed program should:

- Create a local SQLite database file when the application starts.
- Create a `books` table if it does not already exist.
- Store an integer ID, a title, an author, and a publication year for each book.
- Insert sample books only when the table is empty.
- Use parameterized SQL values instead of building SQL statements with string concatenation.

### 🛠️ Connect REST Routes to the Database

#### Description

Replace the starter data source with database queries. Implement endpoints that allow clients to manage books through the API.

#### Requirements

Completed program should:

- Include a `GET /books` route that returns every book from SQLite.
- Include a `GET /books/{book_id}` route that returns one book or a `404` response when it does not exist.
- Include a `POST /books` route that validates a request body and inserts a new book.
- Include a `PUT /books/{book_id}` route that updates an existing book or returns `404` when it does not exist.
- Include a `DELETE /books/{book_id}` route that removes an existing book or returns `404` when it does not exist.
- Close database connections after each request.

### 🛠️ Verify Persistent Behavior

#### Description

Run the API, use the interactive documentation, and confirm that changes remain after the server restarts.

#### Requirements

Completed program should:

- Start successfully with Uvicorn and expose the interactive documentation at `/docs`.
- Use the documentation page to create, read, update, and delete a book.
- Return clear JSON responses and appropriate HTTP status codes for successful and unsuccessful requests.
- Stop and restart the server, then confirm that previously created books are still present.
- Keep the database file out of source control by adding it to a suitable `.gitignore` entry.
