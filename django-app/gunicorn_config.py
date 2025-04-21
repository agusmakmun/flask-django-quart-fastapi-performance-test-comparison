import multiprocessing

# Server socket configuration
bind = "0.0.0.0:8000"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"

# Timeout configuration
timeout = 120
keepalive = 5

# Concurrency settings
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50

# Application
wsgi_app = "wsgi:asgi_app"  # Use the ASGI application from wsgi.py

# Logging
loglevel = "info"
accesslog = "-"
errorlog = "-"

# Process naming
proc_name = "django_gunicorn_app"

# SSL configuration (if needed)
# keyfile = "path/to/keyfile"
# certfile = "path/to/certfile"
