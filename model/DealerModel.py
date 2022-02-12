from pydantic import BaseModel
from dependencies import PyObjectId
from database import db

class DealerInfo(BaseModel):
    userid: PyObjectId
    phoneno: int
    nature_of_material : str
    quantity : int
    city : PyObjectId
    state : PyObjectId

class Dealeruserid(BaseModel):
    userid: PyObjectId

dealerdb = db["dealer_db"]
    