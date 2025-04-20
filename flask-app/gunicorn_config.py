bind = "0.0.0.0:8000"
workers = 4  # Number of worker processes
worker_class = "uvicorn.workers.UvicornWorker"  # Use Uvicorn workers
timeout = 120
keepalive = 5
wsgi_app = "app:asgi_app"  # Use the ASGI wrapped application
