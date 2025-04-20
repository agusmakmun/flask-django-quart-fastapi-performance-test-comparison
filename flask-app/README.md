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
   gunicorn -c gunicorn_config.py
   ```

3. For development with hot reload:
   ```bash
   gunicorn -c gunicorn_config.py --reload
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

## Performance Testing

For performance testing, use the shared script in the root directory:

1. Make sure the application is running with Gunicorn:
   ```bash
   gunicorn -c gunicorn_config.py
   ```

2. Navigate to the root directory and make the performance testing script executable:
   ```bash
   cd ..
   chmod +x test-performance.sh
   ```

3. Run the performance test:
   ```bash
   ./test-performance.sh
   ```

The test will:
- Send requests at configurable rates (default: 9000/s)
- Display real-time metrics including:
  - Requests per second
  - Response status codes
  - Latency percentiles (p25, p50, p95)
  - Bytes in/out

You can modify the rate in the script by changing the `-rate=9000/s` parameter.

## Development Tips

- Use the `--reload` flag during development to automatically reload the server when code changes
- For debugging, you can increase worker timeout using `--timeout 120`
- Monitor worker processes with `--log-level debug`
- The application uses ASGI middleware to ensure compatibility with Uvicorn workers 