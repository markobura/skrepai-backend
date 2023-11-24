from fastapi import APIRouter, HTTPException, status

from app.candidates.database import candidates_collection
from app.candidates.models import Candidate
from app.database import serializeList

router = APIRouter(
    prefix="/candidates",
    tags=['candidates']
)


@router.get("/")
async def get_all_candidates():
    cursor = candidates_collection.find()
    raw_history = await cursor.to_list(length=1000)
    history = serializeList(raw_history)
    if history:
        return history
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No candidates found")


@router.post("/")
async def create_candidate(candidate: Candidate):
    return await candidates_collection.insert_one(candidate.model_dump())
