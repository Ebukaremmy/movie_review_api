🎬 Movie Review API

A secure, searchable, and production-ready RESTful backend for managing movies and authentic user reviews.

Hi, I’m Ebuka Ikegwuonu.
This project was built as my Backend Capstone to solve a common challenge: organizing movie data in a structured way, allowing real users to leave reviews, and protecting the system using modern authentication standards.

🚀 Live Demo:
https://movie-review-api-k2ws.onrender.com

🌟 Features
🍿 Smart Movie Management

Full CRUD Operations – Create, Read, Update, and Delete movies

Search & Filtering – Quickly find movies by title or genre

Pagination – Results are returned in chunks (10 per page) for better performance

RESTful Design – Clean and structured endpoints following best practices

⭐ Real User Reviews

Relational Database Design – Reviews are connected using ForeignKey relationships

Each review is linked to:

A specific movie

A specific authenticated user

Authenticated Reviews Only – Users must be logged in to create reviews

This ensures structured and reliable data management.

🔐 Security & Authentication

JWT Authentication (SimpleJWT)
Secure token-based authentication system

Permission Control

Anyone can browse movies

Only authenticated users can create or modify content

Unauthorized users receive proper HTTP status codes (403 Forbidden / 401 Unauthorized)

🛠 Tech Stack

Backend: Django

API Framework: Django REST Framework

Database (Production): PostgreSQL

Database (Local): SQLite

Authentication: JWT (SimpleJWT)

Deployment: Render

Static File Handling: WhiteNoise

📡 API Endpoints
Endpoint	Method	Description
/	GET	Custom Project Dashboard
/api/movies/	GET, POST	List or create movies
/api/movies/?search=...	GET	Search movies
/api/movies/<id>/	GET, PUT, DELETE	Manage specific movie
/api/reviews/	GET, POST	List or create reviews
/api/token/	POST	Obtain JWT access token
⚙️ Local Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Ebukaremmy/movie_review_api.git
cd movie_review_api
2️⃣ Create and Activate Virtual Environment
python -m venv venv

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies & Run Server
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Server will run at:

http://127.0.0.1:8000/
🎯 Technical Highlights

Structured RESTful API architecture

Proper HTTP status codes (200, 201, 204, 403, 401)

Custom logging configuration for request tracking

Clean database relationships using ForeignKey

Production-ready deployment on Render

Secure environment variable handling

Built with dedication by Ebuka Ikegwuonu 🚀