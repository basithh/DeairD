from fastapi import APIRouter
from model.DriverModel import DriverInfo, driverdb, Driveruserid

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