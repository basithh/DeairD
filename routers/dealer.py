from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

fakedb = []



@router.get("/")
async def dealeroot():
    return {"message": "Hi Vim dealer"}