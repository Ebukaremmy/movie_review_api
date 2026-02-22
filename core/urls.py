from django.contrib import admin
from django.urls import path, include
from reviews.views import home_view  # Import your new view from the reviews app
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # This is the "Home Page" at http://127.0.0.1:8000/
    path('', home_view, name='home'),  
    
    # Admin Panel at http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    
    # Movie Review API endpoints at http://127.0.0.1:8000/api/
    path('api/', include('reviews.urls')),
    
    # JWT Authentication Endpoints (Login)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # JWT Token Refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]