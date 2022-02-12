from pydantic import BaseModel,Field
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# from LocationModel import LocationData
from database import db

class LocationData(BaseModel):
    id: int
    name: str

class RouteData(BaseModel):
    id: int
    tostate: PyObjectId 
    forstate: PyObjectId 
    

routedb = db["route_db"]