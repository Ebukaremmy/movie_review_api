"""
Asynchronous Server Gateway Interface (ASGI) Configuration.

This module provides the asynchronous entry point for ASGI-compliant web servers 
to interface with the application. It exposes the 'application' callable for 
high-performance, asynchronous connectivity.
"""

import os

from django.core.asgi import get_asgi_application

# Configure the environment to use the project's primary settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize the ASGI application for production-ready asynchronous support
application = get_asgi_application()