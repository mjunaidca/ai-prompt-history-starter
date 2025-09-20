from fastapi import FastAPI

app = FastAPI(title="AI Prompt History Starter", version="0.1.0")


@app.get("/hello")
async def hello():
    """Hello World endpoint that returns a simple greeting message."""
    return {"message": "Hello World!"}
