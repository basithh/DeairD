from pydantic import BaseModel
from typing import List
from dependencies import PyObjectId
from database import db

class DriverInfo(BaseModel):
    userid: PyObjectId
    age: int
    trucknumber: str
    truckcap: int
    transportername: str
    experience: int
    interestroute: List[PyObjectId]


class Driveruserid(BaseModel):
    userid: PyObjectId

driverdb = db["driver_db"]






