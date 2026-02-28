from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet

# Initialize the automated routing system for the API
router = DefaultRouter()

# Register resource endpoints for Movie and Review collections
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    # Include all dynamically generated routes from the router
    path('', include(router.urls)),
]