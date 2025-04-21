import os
import django
from django.core.asgi import get_asgi_application

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

# Get the Django ASGI application
asgi_app = get_asgi_application()
