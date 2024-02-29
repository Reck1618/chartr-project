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
- **Description**: Swagger UI provides interactive documentation for exploring the endpoints and testing the API directly from your browser.

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
```

## Getting Started On Local

- Clone the repository.
- Create a Python virtual environment.
```
python -m venv env
```
- Activate the virtual environment
```
source env/bin/activate 
```
- Install the Dependencies.
```
pip install -r requirements.txt
```
- Run Migrations
```
python manage.py migrate
```
- Run the Development Server
```
python manage.py runserver
```
- Access the API
  - you can now access the API at 'http://localhost:8000/api/v1/notes/'
  - if you access localhost:8000 it will redirect to the API

## Error Handling
- The API returns appropriate HTTP status codes for different types of errors.
- Error responses include a descriptive message in the JSON format.

## Testing
- Unit tests are included in the tests.py file.
- Run tests using the command:
```
python manage.py test
```

## Production Environment
- This API is not production-ready and is only suitable for the development environment.
- You can configure the production environment according to your needs **URL** [SET UP PRODUCTION ENVIRONMENT](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
  
## Deployment
- Choose your preferred deployment method (e.g., Heroku, AWS, etc.).
- Configure your deployment environment.
- Deploy your Django project according to the platform-specific instructions.
- Make sure to set up necessary environment variables, database configurations, and any other settings required for deployment.
- For more help **URL** [Deploy Django](https://docs.djangoproject.com/en/5.0/howto/deployment/)

## Additional Information
- Authentication: This API does not require authentication.

