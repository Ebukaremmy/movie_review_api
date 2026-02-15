from django.contrib import admin
from .models import Movie, Review

# This registers the models so they appear in the /admin interface
admin.site.register(Movie)
admin.site.register(Review)