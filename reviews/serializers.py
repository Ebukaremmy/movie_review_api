from rest_framework import serializers
from .models import Movie, Review
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # This makes the username and movie title show up as text instead of just ID numbers
    user_name = serializers.ReadOnlyField(source='user.username')
    movie_title = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Review
        model = Review
        fields = ['id', 'user', 'user_name', 'movie', 'movie_title', 'rating', 'comment', 'created_at']
        # This ensures the 'user' field is handled automatically by the view, not the user input
        read_only_fields = ['user']