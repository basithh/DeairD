from pydantic import BaseModel
from database import db

class LocationData(BaseModel):
    id: int
    name: str

locationdb = db["location_db"]




