# GigRadar
GigRadar is a freelance job aggregator and application tracker API built with FastAPI. It lets users register, browse and search freelance gigs, bookmark listings, and track their application pipeline from applied to interview to hired/rejected.

## Features

- **User Authentication** — Register/login with JWT access tokens, OAuth2 password flow, bcrypt password hashing
- **Gig Management** — Full CRUD for job listings with nested client/tag data
- **Application Tracking** — Track application status per gig (applied → interview → rejected/hired)
- **Robust Error Handling** — Centralized exception handlers for consistent API response
---

## Tech Stack

| Layer          | Technology                          |
|----------------|--------------------------------------|
| Framework      | FastAPI                              |
| Language       | Python 3.11+                         |
| Database       | PostgreSQL + SQLAlchemy ORM          |
| Auth           | JWT (python-jose), OAuth2, Passlib   |
| Validation     | Pydantic v2                          |
| Testing        | Pytest, httpx                        |
                              

---

## Project Structure

```
gigradar/
├── app/
│   ├── main.py               # App entrypoint, middleware, exception handlers
│   ├── database.py           # DB engine & session setup
│   ├── models/                # SQLAlchemy models
│   │   ├── user.py
│   │   ├── gig.py
│   │   └── application.py
│   ├── schemas/                # Pydantic request/response models
│   │   ├── user.py
│   │   ├── gig.py
│   │   └── application.py
│   ├── routers/                 # API route modules
│   │   ├── auth.py
│   │   ├── gigs.py
│   │   └── applications.py
│   ├── auth/                    # JWT + password hashing utilities
│   │   ├── jwt_handler.py
│   │   └── dependencies.py
│              
├── tests/
│   ├── test_auth.py
│   └── test_gigs.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL running locally or a hosted instance
- pip / virtualenv

### Installation

```bash
# Clone the repository
git clone https://github.com/mirajkhan/gigradar.git
cd gigradar

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root (see `.env.example`):

```env
DATABASE_URL=postgresql://user:password@localhost:5432/gigradar
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run the App

```bash
uvicorn app.main:app --reload
```

The API will be live at `http://127.0.0.1:8000`
Interactive docs (Swagger UI) at `http://127.0.0.1:8000/docs`

---

## API Endpoints (Overview)

| Method | Endpoint                     | Description                        | Auth Required |
|--------|-------------------------------|-------------------------------------|----------------|
| POST   | `/auth/register`              | Register a new user                 | No             |
| POST   | `/auth/login`                 | Login and receive JWT token         | No             |
| GET    | `/gigs`                       | List/search gigs (paginated)        | Yes            |
| POST   | `/gigs`                       | Create a new gig                    | Yes            |
| GET    | `/gigs/{id}`                  | Get a single gig                    | Yes            |
| PUT    | `/gigs/{id}`                  | Update a gig                        | Yes            |
| DELETE | `/gigs/{id}`                  | Delete a gig                        | Yes            |
| POST   | `/applications`               | Create an application               | Yes            |
| GET    | `/applications`               | List user's applications            | Yes            |
| PUT    | `/applications/{id}`          | Update application status           | Yes            |
| POST   | `/users/me/resume`            | Upload resume/portfolio file        | Yes            |

Full request/response schemas are available via the Swagger UI at `/docs`.

---

## Running Tests

```bash
pytest -v
```

---

## Deployment

This project is configured for deployment on **Render**:

1. Push the repository to GitHub
2. Create a new Web Service on Render, connect the repo
3. Set the build command: `pip install -r requirements.txt`
4. Set the start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables (`DATABASE_URL`, `SECRET_KEY`, etc.) in the Render dashboard

---

## Author

**Miraj Khan**

---

## License

This project is licensed under the MIT License.
