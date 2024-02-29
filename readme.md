# Note Taking API

This is a simple note-taking API built using Django and Django REST Framework. It allows users to create, retrieve, update, patch, and delete notes.

## Endpoints

- `POST /api/v1/notes/`: Create a new note.
- `GET /api/v1/notes/`: Retrieve a list of all notes.
- `GET /api/v1/notes/<pk>/`: Retrieve a specific note by its primary key.
- `PUT /api/v1/notes/<pk>/`: Update a specific note by its primary key.
- `PATCH /api/v1/notes/<pk>/`: Patch a specific note by its primary key.
- `DELETE /api/v1/notes/<pk>/`: Delete a specific note by its primary key.

## Querying Notes

- You can query notes by title substring using the `title` query parameter:
  - Example: `GET /api/v1/notes/?title=search_string`

## Swagger Documentation

You can explore the API documentation using Swagger UI:

- **URL**: [Swagger Documentation](http://localhost:8000/swagger/)
- **Description**: Swagger UI provides an interactive documentation for exploring the endpoints and testing the API directly from your browser.

## Request and Response Formats

- Requests should be in JSON format.
- Responses will be in JSON format.

### Note Object

```json
{
  "id": 1,
  "title": "Example Note",
  "body": "This is the body of the note.",
  "created_at": "2024-02-29T12:00:00Z",
  "updated_at": "2024-02-29T12:00:00Z"
}
