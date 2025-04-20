# Flask Application with Gunicorn and Uvicorn

This is a simple Flask application that demonstrates the use of Gunicorn with Uvicorn workers.

## Features

- Simple dummy API endpoint at `/api/dummy`
- Uses Gunicorn as the WSGI HTTP server
- Implements Uvicorn workers for improved performance
- Configurable through gunicorn_config.py
- ASGI compatibility for better performance with Uvicorn

## Installation

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   # or
   .\venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode (Flask Built-in Server)
To run the application in development mode with Flask's built-in server:
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000`

### Local Development with Gunicorn
There are several ways to run the application locally with Gunicorn:

1. Basic Gunicorn command:
   ```bash
   gunicorn app:asgi_app --bind 127.0.0.1:8000 --worker-class uvicorn.workers.UvicornWorker
   ```

2. Using Gunicorn with configuration file (recommended):
   ```bash
   gunicorn --bind 127.0.0.1:8000 -c gunicorn_config.py
   ```

3. For development with hot reload:
   ```bash
   gunicorn --bind 127.0.0.1:8000 -c gunicorn_config.py --reload
   ```

The application will be available at `http://127.0.0.1:8000`

### Production Mode
To run the application in production mode:
```bash
gunicorn -c gunicorn_config.py
```
The application will be available at `http://0.0.0.0:8000`

## Testing the API

You can test the dummy endpoint using curl:
```bash
# If running locally with Gunicorn
curl http://127.0.0.1:8000/api/dummy

# If running in production mode
curl http://localhost:8000/api/dummy
```

Expected response:
```json
{
    "message": "Hello from dummy endpoint!",
    "status": "success"
}
```

## Development Tips

- Use the `--reload` flag during development to automatically reload the server when code changes
- For debugging, you can increase worker timeout using `--timeout 120`
- Monitor worker processes with `--log-level debug`
- The application uses ASGI middleware to ensure compatibility with Uvicorn workers 