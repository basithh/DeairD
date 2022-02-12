from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from DriverModel import DriverInfo
from DealerModel import DealerInfo
from RouteModel import RouteData
from database import Base

class Booking(Base):
    id = Column(Integer, primary_key=True)
    truckid = relationship()
    dealerid: DealerInfo
    agreestatus: bool
    route: RouteData

class Job(Base):
    __tablename__ = 'location2'

    id = Column(Inte, primary_key=True)
    name = Column(String, nullable=False)
    name2 = Column(String, nullable=False)

