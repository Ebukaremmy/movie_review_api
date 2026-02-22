# 🎬 Movie Review API

A RESTful API built with Django and Django REST Framework that allows users to register, authenticate, browse movies, and create reviews.

This project was built as part of the ALX Backend Capstone.

---

## 🚀 Features

### 🔐 Authentication
- User registration
- User login with JWT authentication
- Protected routes for authenticated users

### 🎬 Movies
- Create a movie
- Retrieve all movies
- Retrieve a single movie
- Update a movie
- Delete a movie

### ⭐ Reviews
- Authenticated users can create reviews
- Users can update or delete only their own reviews
- Each review is linked to a specific movie
- Prevents duplicate reviews per user per movie

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL (or SQLite for development)
- JWT Authentication (SimpleJWT)

---

## 📂 Project Structure

```
movie_review_api/
│
├── config/
├── users/
├── movies/
├── reviews/
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ebukaremmy/movie-review-api.git
cd movie-review-api
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the development server

```bash
python manage.py runserver
```

Server will run at:
```
http://127.0.0.1:8000/
```

---

## 🔑 Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /api/register/ | Register new user |
| POST | /api/token/ | Obtain JWT token |
| POST | /api/token/refresh/ | Refresh token |

---

## 🎬 Movie Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /api/movies/ | List all movies |
| POST | /api/movies/ | Create movie |
| GET | /api/movies/<id>/ | Retrieve single movie |
| PUT | /api/movies/<id>/ | Update movie |
| DELETE | /api/movies/<id>/ | Delete movie |

---

## ⭐ Review Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /api/reviews/ | List reviews |
| POST | /api/reviews/ | Create review |
| PUT | /api/reviews/<id>/ | Update review |
| DELETE | /api/reviews/<id>/ | Delete review |

---

## 📌 Future Improvements

- Movie average rating calculation
- Pagination and filtering
- Search functionality
- Unit testing
- Deployment to cloud platform

---

## 👨‍💻 Author

Ebuka Ikegwuonu  
ALX Backend Engineering Program