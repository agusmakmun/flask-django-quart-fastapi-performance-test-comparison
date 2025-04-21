import os
import django
from django.core.asgi import get_asgi_application

# from django.core.wsgi import get_wsgi_application
# from asgiref.wsgi import WsgiToAsgi

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

# Get the Django ASGI application (primary approach)
asgi_app = get_asgi_application()

# Alternative approach using WsgiToAsgi (uncomment if needed)
# wsgi_app = get_wsgi_application()
# asgi_app = WsgiToAsgi(wsgi_app)

# For direct execution
if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
