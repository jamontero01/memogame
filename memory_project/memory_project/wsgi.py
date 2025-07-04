"""WSGI entry point for the Memory Game project."""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memory_project.settings')

application = get_wsgi_application()
