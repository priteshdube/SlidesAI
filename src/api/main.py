import fastapi
from fastapi.middleware.cors import CORSMiddleware
from agents.summarizer import Summarizer
from src.api.routes import router as api_router
import uvicorn


app = fastapi.FastAPI(title="SlidesAI", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to SlidesAI"}

if __name__ == "__main__":
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, reload=True)

