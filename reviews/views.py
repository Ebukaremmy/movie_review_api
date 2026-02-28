from django.http import HttpResponse
from rest_framework import viewsets, permissions, filters
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

# --- API VIEWS ---

class MovieViewSet(viewsets.ModelViewSet):
    """
    Handles full CRUD (Create, Read, Update, Delete) for movies.
    Permissions: Anyone can view, but only authenticated users can add/edit.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Enables the Search Bar and Ordering in the "Filters" button
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'genre']
    ordering_fields = ['release_year', 'title']

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Handles full CRUD for reviews.
    Permissions: Anyone can view, but only authenticated users can post reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically links the review to the user currently logged in via JWT
        serializer.save(user=self.request.user)


# --- HOME PAGE VIEW ---

def home_view(request):
    """
    A clean landing page for the root URL providing navigation.
    """
    return HttpResponse("""
        <html>
            <head>
                <style>
                    body { font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto; }
                    h1 { color: #2c3e50; }
                    ul { list-style: none; padding: 0; }
                    li { background: #f4f4f4; margin: 5px 0; padding: 10px; border-radius: 5px; }
                    a { text-decoration: none; color: #3498db; font-weight: bold; }
                    a:hover { color: #2980b9; }
                </style>
                <title>Movie Review API</title>
            </head>
            <body>
                <h1>Welcome to the Movie Review API</h1>
                <p>Hello, I'm Ebuka. This is my Capstone Project showing a full CRUD API with Search and JWT Auth.</p>
                <h3>API Endpoints:</h3>
                <ul>
                    <li><a href='/api/movies/'>Movies API</a> - View all movies or add new ones (POST)</li>
                    <li><a href='/api/reviews/'>Reviews API</a> - View and write reviews</li>
                    <li><a href='/api/token/'>Auth Token</a> - Get your JWT Access Token</li>
                    <li><a href='/admin/'>Admin Panel</a> - Management Dashboard</li>
                </ul>
            </body>
        </html>
    """)