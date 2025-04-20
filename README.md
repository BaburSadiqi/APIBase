#  FastAPI PostgreSQL Starter

This is a simple starter project using **FastAPI** with **SQLAlchemy** and **PostgreSQL**, designed for building robust APIs quickly and efficiently.

---

##  Tech Stack

- **FastAPI** – Modern Python web framework
- **SQLAlchemy** – ORM (Object Relational Mapper)
- **PostgreSQL** – Open-source relational database
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server for running FastAPI apps

---

##  Project Structure

```
.
├── main.py              # FastAPI app entry point
├── database.py          # SQLAlchemy database configuration
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── routers/             # Route handlers
├── env/                 # Python virtual environment (should be excluded from Git)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

##  Requirements

- Python 3.8 or newer
- PostgreSQL installed and running
- Git (for version control)
- VS Code (recommended editor)

---

## ⚙ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-postgresql-starter.git
cd fastapi-postgresql-starter
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
env\Scripts\activate       # Windows
# or
source env/bin/activate    # Mac/Linux
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

Or use a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure the database

In `database.py`, update the connection string with your PostgreSQL credentials:

```python
DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/your_database"
```

Make sure the database exists in PostgreSQL.

### 5. Run the application

```bash
uvicorn main:app --reload
```

Then open your browser and go to:

```
http://127.0.0.1:8000
```

Swagger docs are available at:

```
http://127.0.0.1:8000/docs
```

---

##  Common GitHub & Git Tips

### Exclude your virtual environment from Git:

Create a `.gitignore` file (if not exists) and add:

```
env/
__pycache__/
*.pyc
```

### Avoid Git errors with CRLF/LF line endings:

```bash
git config --global core.autocrlf true
```

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

**Babur Sadiqi**

If you found this useful, feel free to give it a ⭐ on GitHub!
