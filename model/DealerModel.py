from pydantic import BaseModel
from LocationModel import LocationData

class DealerInfo(BaseModel):
    id: int
    name: str
    phoneno: int
    nature_of_material : str
    quantity : int
    city : str
    state : LocationData