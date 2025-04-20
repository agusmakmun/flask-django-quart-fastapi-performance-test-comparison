# FastAPI Application with Gunicorn and Uvicorn

This is a FastAPI application that demonstrates high-performance API development with modern Python frameworks.

## Features

- Async API endpoint at `/api/dummy`
- Uses Gunicorn with Uvicorn workers for optimal performance
- Native ASGI support through FastAPI
- Includes performance testing setup with Vegeta

## Prerequisites

Before running the application, make sure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Homebrew (for macOS users, needed for performance testing tools)

For performance testing, you'll need these additional tools:
```bash
# Install Vegeta (HTTP load testing tool)
brew update && brew install vegeta

# Install plotting tools
brew install rs/tap/jaggr
brew install rs/tap/jplot
```

## Project Structure

```
.
├── app.py              # Main FastAPI application file
├── gunicorn_config.py  # Gunicorn server configuration
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Installation

1. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it on macOS/Linux
   source venv/bin/activate
   
   # Or on Windows
   .\venv\Scripts\activate
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode
Run with Uvicorn directly:
```bash
uvicorn app:app --reload
```
Access at: http://127.0.0.1:8000

### Production Mode
Run with Gunicorn (recommended for production):
```bash
# Basic usage
gunicorn app:app --bind 127.0.0.1:8000 --worker-class uvicorn.workers.UvicornWorker

# Using configuration file (recommended)
gunicorn -c gunicorn_config.py

# With hot reload for development
gunicorn -c gunicorn_config.py --reload
```
Access at: http://127.0.0.1:8000

## API Endpoints

### GET /api/dummy
Returns a simple JSON response.

Example request:
```bash
curl http://127.0.0.1:8000/api/dummy
```

Example response:
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

## Configuration

### Gunicorn Settings
Key settings in `gunicorn_config.py`:
- Workers: `cpu_count * 2 + 1`
- Worker class: `uvicorn.workers.UvicornWorker`
- Max requests: 1000
- Timeout: 120 seconds
- Keep-alive: 5 seconds

## Troubleshooting

1. If you see "Address already in use":
   ```bash
   # Find and kill the process using the port
   lsof -i :8000
   kill -9 <PID>
   ```

2. If performance test script fails:
   - Ensure Vegeta and plotting tools are installed
   - Check if the application is running
   - Verify the endpoint URL in the script

## Development Tips

- Use `--reload` flag during development for auto-reloading
- Monitor logs with `--log-level debug`
- Check Gunicorn error logs if the server fails to start
- For production, adjust worker count based on your server's resources 