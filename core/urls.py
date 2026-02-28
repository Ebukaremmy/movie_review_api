from django.contrib import admin
from django.urls import path, include
from reviews.views import home_view 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Application Entry Point: Root landing page for the project
    path('', home_view, name='home'),  
    
    # Administrative Interface: Secure management portal for database records
    path('admin/', admin.site.urls),
    
    # API Routing: Delegation of requests to the internal Review System module
    path('api/', include('reviews.urls')),
    
    # Authentication Services: Endpoint for obtaining JWT access and refresh tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Token Lifecycle Management: Endpoint for renewing expired access tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]