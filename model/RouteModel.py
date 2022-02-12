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
    
#locationdb = db["location_db"]
routedb = db["route_db"]
citydb = db["city_db"]
statedb = db["state_db"]
