"""
Web Server Gateway Interface (WSGI) Configuration.

This module provides the entry point for WSGI-compliant web servers to serve 
the application. It exposes the 'application' callable, which interfaces 
between the web server and the Django framework.
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the configuration of the application environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize the WSGI application for production deployment
application = get_wsgi_application()