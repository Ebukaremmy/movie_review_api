from django.http import HttpResponse
from rest_framework import viewsets, permissions, filters
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

# --- API VIEWS ---

class MovieViewSet(viewsets.ModelViewSet):
    """
    Handles full CRUD (Create, Read, Update, Delete) for movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # These lines enable the Search UI and Ordering in the browsable API
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'genre']
    ordering_fields = ['release_year', 'title']

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Handles full CRUD for reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically links the review to the user currently logged in
        serializer.save(user=self.request.user)


# --- HOME PAGE VIEW ---

def home_view(request):
    """
    A clean dashboard for navigating the API endpoints.
    """
    return HttpResponse("""
        <html>
            <head>
                <style>
                    body { font-family: sans-serif; line-height: 1.6; padding: 40px; max-width: 800px; margin: auto; background-color: #f8f9fa; }
                    .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
                    h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
                    ul { list-style: none; padding: 0; }
                    li { margin: 15px 0; }
                    a { text-decoration: none; color: #3498db; font-weight: bold; font-size: 1.1em; }
                    a:hover { color: #2c3e50; }
                </style>
                <title>Movie Review API</title>
            </head>
            <body>
                <div class="card">
                    <h1>Movie Review API Dashboard</h1>
                    <p>Select an endpoint below to interact with the API documentation and resources.</p>
                    <ul>
                        <li><a href='/api/movies/'>📁 Movies Endpoint</a></li>
                        <li><a href='/api/reviews/'>💬 Reviews Endpoint</a></li>
                        <li><a href='/api/token/'>🔑 Authentication (JWT)</a></li>
                        <li><a href='/admin/'>⚙️ Admin Control Panel</a></li>
                    </ul>
                </div>
            </body>
        </html>
    """)