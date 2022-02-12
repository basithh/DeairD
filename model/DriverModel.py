from pydantic import BaseModel
from dependencies import PyObjectId
from database import db

# course model to store courses
class DriverInfo(BaseModel):
    userid: PyObjectId
    age: int
    trucknumber: str
    phoneno: int
    truckcap: int
    transportername: str
    experience: int
    interestroute: list=[PyObjectId]

class Driveruserid(BaseModel):
    userid: PyObjectId

driverdb = db["driver_db"]






