from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This enables the admin panel
    path('api/', include('reviews.urls')), # This connects your reviews app
]