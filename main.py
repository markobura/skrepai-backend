from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.candidate_routes import router as candidate_router

app = FastAPI()

app.include_router(candidate_router)


@app.get("/health-check")
async def health_check():
    return {"message": "Running..."}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
