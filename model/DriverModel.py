from pydantic import BaseModel
from RouteModel import RouteData

# course model to store courses
class DriverInfo(BaseModel):
    id: int
    name: str
    age: int
    Trucknumber: str
    phoneno: int
    truckcap: int
    transportername: str
    experience: int
    interestroute: list=[RouteData]


