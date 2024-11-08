# TodoList API Project

A Django REST framework-based API for managing todo lists with user authentication and comprehensive test coverage.

## Features

- User authentication with JWT tokens
- Task management (CRUD operations)
- Comments on tasks
- Task tagging system
- Filtering, searching, and ordering tasks
- Swagger/ReDoc API documentation
- Type hints with mypy validation
- Comprehensive test coverage

## Technology Stack

- Python 3.12
- Django 5.0
- Django REST framework
- PostgreSQL
- JWT Authentication
- Swagger/ReDoc for API documentation
- Black, isort, flake8 for code formatting
- Mypy for type checking

## Setup

1. Clone the repository:
```bash
git clone https://github.com/maria-v-ch/taskforge-api
cd todolist
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy environment variables:
```bash
cp .env.sample .env
```

5. Set up the database:
```bash
cd todolist
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Documentation

- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register new user
- `POST /api/users/token/` - Obtain JWT token
- `POST /api/users/token/refresh/` - Refresh JWT token

### Tasks
- `GET /api/tasks/` - List tasks
- `POST /api/tasks/` - Create task
- `GET /api/tasks/{id}/` - Retrieve task
- `PUT/PATCH /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task
- `POST /api/tasks/{id}/add_comment/` - Add comment to task

### Comments
- `GET /api/comments/` - List comments
- `POST /api/comments/` - Create comment
- `GET /api/comments/{id}/` - Retrieve comment
- `PUT/PATCH /api/comments/{id}/` - Update comment
- `DELETE /api/comments/{id}/` - Delete comment

### Tags
- `GET /api/tags/` - List tags
- `POST /api/tags/` - Create tag
- `GET /api/tags/{id}/` - Retrieve tag
- `PUT/PATCH /api/tags/{id}/` - Update tag
- `DELETE /api/tags/{id}/` - Delete tag

## Development

### Running Tests
```bash
python manage.py test
```

### Code Quality Checks
```bash
pre-commit run --all-files
```

### Type Checking
```bash
mypy todolist
```

## Project Structure

```
todolist/
├── todolist/              # Project configuration
├── todolist_app/          # Main application
│   ├── migrations/
│   ├── management/
│   ├── models.py          # Database models
│   ├── serializers.py     # API serializers
│   ├── views.py           # API views
│   ├── permissions.py     # Custom permissions
│   └── tests.py          # Tests
└── users/                # User management app
    ├── migrations/
    ├── models.py         # Custom user model
    ├── serializers.py    # User serializers
    ├── views.py         # User views
    └── tests.py         # User tests
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and code quality checks
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
