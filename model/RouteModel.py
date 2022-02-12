from pydantic import BaseModel
from dependencies import PyObjectId

# from LocationModel import LocationData
from database import db

class LocationData(BaseModel):
    id: int
    state: str

class RouteData(BaseModel):
    id: int
    tostate: PyObjectId 
    forstate: PyObjectId 
    

routedb = db["route_db"]