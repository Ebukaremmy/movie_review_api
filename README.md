🎬 Movie Review API

Hi, I’m Ebuka Ikegwuonu, and this is my Backend Capstone Project.

I built this API to provide movie lovers with a clean, secure, and scalable system where they can explore movies and share authentic reviews.

🚀 Live Demo:
https://movie-review-api-k2ws.onrender.com

🌟 Features
🎬 Browse Movies

View movie titles, descriptions, and genres.

Scalable structure designed to handle large datasets.

⭐ Write Reviews

Authenticated users can submit ratings and comments.

Each review is linked to a specific movie and user.

🔐 Secure Authentication

Implemented JWT (JSON Web Token) authentication.

Only authenticated users can create, update, or delete reviews.

⚡ Pagination for Performance

The API loads data in manageable chunks.

Ensures fast performance even with thousands of records.

🛠 Admin Dashboard

Built-in Django Admin interface.

Full control over users, movies, and reviews.

🛠 Tech Stack

Framework: Django & Django REST Framework

Database: PostgreSQL (Production), SQLite (Development)

Authentication: JWT (SimpleJWT)

Deployment: Render

⚙️ Local Setup Instructions

To run this project locally:

1️⃣ Clone the Repository
git clone https://github.com/Ebukaremmy/movie_review_api.git
cd YOUR-REPO-NAME
2️⃣ Create & Activate Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Migrations
python manage.py migrate
5️⃣ Start the Development Server
python manage.py runserver

Visit:

http://127.0.0.1:8000/
📡 Key API Endpoints
Endpoint	Description
/api/movies/	List and manage movies
/api/reviews/	List and manage reviews
/api/token/	Obtain JWT access token
/admin/	Admin dashboard
🎯 Project Highlights

This project demonstrates:

RESTful API design

Relational database modeling

JWT authentication & security

Pagination for scalability

Deployment to a live production environment

Built with dedication by Ebuka Ikegwuonu 🚀