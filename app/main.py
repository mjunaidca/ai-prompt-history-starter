from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI(title="AI Prompt History Starter", version="0.1.0")


@app.get("/hello")
async def hello(name: str = Query(None, description="Optional name parameter")):
    """Hello World endpoint that returns a greeting message with optional name."""
    message = f"Hello {name}!" if name else "Hello World!"
    
    return {
        "message": message,
        "status": "success",
        "timestamp": datetime.now().isoformat() + "Z",
        "version": "0.1.0"
    }


@app.post("/hello")
async def hello_post():
    """Hello World POST endpoint that returns a greeting message."""
    return {
        "message": "Hello World!",
        "status": "success",
        "timestamp": datetime.now().isoformat() + "Z",
        "version": "0.1.0"
    }
