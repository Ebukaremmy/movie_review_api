from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

# --- API VIEWS ---

class MovieViewSet(viewsets.ModelViewSet):
    """
    Handles viewing and editing movies.
    Permissions: Anyone can view, but only authenticated users can add/edit.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Handles viewing and editing reviews.
    Permissions: Anyone can view, but only authenticated users can post reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # Ensures only authenticated users can POST, but everyone can GET
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
            <head><title>Movie Review API</title></head>
            <body>
                <h1>Welcome to the Movie Review API</h1>
                <h3>Quick Links:</h3>
                <ul>
                    <li><a href='/admin/'>Admin Panel</a> (Manage Movies & Users)</li>
                    <li><a href='/api/movies/'>Movies API</a> (List of all movies)</li>
                    <li><a href='/api/reviews/'>Reviews API</a> (User reviews)</li>
                    <li><a href='/api/token/'>Auth Token</a> (Login for API)</li>
                </ul>
            </body>
        </html>
    """)