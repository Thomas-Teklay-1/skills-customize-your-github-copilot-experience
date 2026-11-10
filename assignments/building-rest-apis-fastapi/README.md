# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with the FastAPI framework. You will practice defining routes, validating request data with Pydantic models, returning JSON responses, and using automatically generated API documentation.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Use the provided starter file to create an API for a collection of books. Start the application with Uvicorn and confirm that the API responds to requests.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Include a root route at `/` that returns a JSON welcome message.
- Include a `GET /books` route that returns the available books as a JSON list.
- Start successfully with Uvicorn without syntax or import errors.

### 🛠️ Add Book Routes and Validation

#### Description

Expand the API so clients can retrieve one book, add a new book, and update an existing book. Use a Pydantic model to validate data sent by clients.

#### Requirements

Completed program should:

- Define a Pydantic model with required fields for a book, such as `title`, `author`, and `year`.
- Include a `GET /books/{book_id}` route that returns one book or a clear error when the ID does not exist.
- Include a `POST /books` route that validates the request body and adds a new book.
- Include a `PUT /books/{book_id}` route that updates an existing book or returns an error when the ID does not exist.
- Return appropriate HTTP status codes for successful requests and missing books.

### 🛠️ Test the Interactive Documentation

#### Description

Use FastAPI's generated documentation to test each route and make sure the API is understandable to another developer.

#### Requirements

Completed program should:

- Open the Swagger UI at `/docs` while the server is running.
- Use the documentation page to test successful and unsuccessful requests for each book route.
- Include clear route names and response messages that explain what each endpoint does.
