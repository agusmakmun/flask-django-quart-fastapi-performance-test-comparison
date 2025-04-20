from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="FastAPI Performance Test")


@app.get("/api/dummy")
async def dummy_endpoint():
    return JSONResponse(
        content={"message": "Hello from dummy endpoint!", "status": "success"}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
