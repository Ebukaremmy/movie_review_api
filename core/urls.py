from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Movie Review API endpoints
    path('api/', include('reviews.urls')),
    
    # JWT Authentication Endpoints
    # Use this to get your 'access' and 'refresh' tokens (Login)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Use this to get a new access token when the old one expires
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]