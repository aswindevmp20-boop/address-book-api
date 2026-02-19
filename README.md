# Address Book API

A minimal RESTful API built using FastAPI that allows users to manage an address book with geographic coordinates.

The application supports:

- Creating addresses
- Updating addresses
- Deleting addresses
- Retrieving all addresses (with pagination)
- Searching addresses within a given distance using geographic coordinates
- UUID-based identifiers
- SQLite database persistence
- Input validation using Pydantic
- Interactive Swagger documentation

---

## Setup & Run Instructions

Create Virtual Environment
python -m venv venv

Activate Virtual Environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Configure Environment Variables
Create a .env file in the project root with the following content:
DATABASE_URL=sqlite:///./addresses.db

Run the Application
uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

Swagger UI documentation:
http://127.0.0.1:8000/docs

## Run Using Docker (Optional)

Build Docker Image
docker build -t address-book-api .

Run Container
docker run -p 8000:8000 address-book-api
