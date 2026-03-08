# Project Creation System

##  Overview

This project is a simple Project_creation System built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
It provides secure JWT-based authentication and RESTful APIs to manage:

- User registration and login
- Project access
- Project creation
- Project update
- Project delete

The system ensures that authenticated users can only update and delete their own project data.

---

##  Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- Postman (`Testing`)

---

##  Features

- Custom User Model (Email-based authentication)
- JWT Authentication
- CRUD APIs for Projects
- Secure access control
- PostgreSQL database integration
- Environment variable configuration

---

##  Project Structure

* Project_Creation_System
    * accounts(Custom user and authentication) 
    * core 
        * Projects
        
    * project_creation_system(Project settings) 
    * manage.py
    * README.md
    * requirements.txt

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd Project_Creation_System 
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. PostgreSQL Configuration
Create PostgreSQL database:

```bash
CREATE DATABASE ProjectCreation_db;
```
Update settings.py:
```bash
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```
### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
Create superuser
```bash
python manage.py createsuperuser
```
### 6. Run Server

```bash
python manage.py runserver

```
---
##  Database Schema

The project uses PostgreSQL as the database.
The application stores project information in the Project table.
Each project is linked to a user using a foreign key (creator_id).
This ensures that users can only access their own projects.

#### Project Table
| Column      | Type         | Description                                 |
| ----------- | ------------ | ------------------------------------------- |
| id          | Integer (PK) | Unique identifier for the project           |
| title       | VARCHAR      | Project title                               |
| description | TEXT         | Project description                         |
| status      | VARCHAR      | Project status (active / inactive)          |
| duration    | Integer      | Project duration in months                  |
| creator_id  | Integer (FK) | References the user who created the project |
| created_at  | Timestamp    | Automatically stores creation time          |

####    Relationships

Each Project belongs to one User. A User can create multiple projects.

User (1) -------- (Many) Project

---
##  API endpoint list

Base URL:


```bash
http://127.0.0.1:8000/projects/

```

| Method | Endpoint          | Description                                             |
| ------ | ----------------- | ------------------------------------------------------- |
| GET    | `/projects/`      | Retrieve all projects created by the authenticated user |
| POST   | `/projects/`      | Create a new project                                    |
| GET    | `/projects/{id}/` | Retrieve a specific project                             |
| PUT    | `/projects/{id}/` | Update a project completely                             |
| PATCH  | `/projects/{id}/` | Update some fields of a project                         |
| DELETE | `/projects/{id}/` | Delete a project                                        |


### Example Request

#### Create Project


```bash
[POST]   http://127.0.0.1:8000/projects/

```

Request body:
```bash
{
  "title": "Python",
  "description": "This is a python project",
  "status": "active",
  "duration": 6
}
```
---
##  Permission Logic

The API uses authentication and object-level permissions to ensure that users can only manage their own projects.

### Rules
1.  User can login by their email ID.

2.  Only authenticated users can access the API.

3.  Authenticated users can view created projects.

4.  When a project is created, the creator field is automatically set to the logged-in user.

5.  Users cannot update or delete projects created by other users.