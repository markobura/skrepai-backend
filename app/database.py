from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("MONGODB_URL", "mongodb://localhost:27017"))
skrepai_db = client.skrepai_database


def serializeDict(a) -> dict:
    return {
        **{i: str(a[i]) for i in a if i == "_id"},
        **{i: a[i] for i in a if i != "_id"},
    }


def serializeList(x) -> list:
    return [serializeDict(a) for a in x]
