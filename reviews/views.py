from rest_framework import viewsets, permissions
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

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