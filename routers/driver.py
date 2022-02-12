from fastapi import APIRouter
from pydantic import BaseModel
from model.DriverModel import DriverInfo, driverdb, Driveruserid
from typing import Optional
from model.UserModel import userdb
from commonschema import serializeDict



router = APIRouter()

@router.post("/register")
async def driver_register(driver: DriverInfo):
    driverdb.insert_one(dict(driver))
    return {"message": "Sucess", "code": 106}


@router.post("/checkdriver")
async def find_for_driver(userid: Driveruserid):
    checkdriver =  driverdb.find_one(dict(userid))
    if (checkdriver):
        return {"driver":checkdriver['_id'],'code':107}
    else:
        return {"message":"Not sucess","code":108}