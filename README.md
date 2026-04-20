##Project Overview
This project designed to implement a RESTful API for managing technical events and conferences using Django and Django REST Framework and to fullfill the technical asessment.
---

## Setup Instructions

1. Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
venv\Scripts\activate   # Windows
4. Install Dependencies
pip install -r requirements.txt
5. Run Migrations
python manage.py makemigrations
python manage.py migrate
6. Create Superuser
python manage.py createsuperuser
7. Run Server
python manage.py runserver

---

## API Documentation

### Base URL
http://127.0.0.1:8000/

### Endpoint

#### 1. Get All Data
- Method: GET
- URL: /api/items/
- Description: Mengambil semua data

#### 2. Create Data
- Method: POST
- URL: /api/items/
- Body:
{
  "name": "example",
  "value": 123
}

#### 3. Update Data
- Method: PUT
- URL: /api/items/{id}/

#### 4. Delete Data
- Method: DELETE
- URL: /api/items/{id}/

---

## Testing Instructions

You can test the API using:

Django REST Framework browser interface
Postman

Suggested test cases:

Register same attendee twice → should fail
Register beyond capacity → should fail
Create overlapping sessions → should fail

---

## Assumptions & Decisions
- Each attendee is uniquely identified by email per event
- Sessions cannot overlap within the same event
- Event capacity is strictly enforced
- SQLite is used for simplicity in development
