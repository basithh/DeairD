from fastapi import APIRouter
from model.DealerModel import dealerdb, Dealeruserid, DealerInfo
from model.RouteModel import  statedb,citydb
from commonschema import serializeLists, serializeList
from dependencies import PyObjectId
from bson import ObjectId

router = APIRouter()


@router.post("/register")
async def dealer_register(dealer: DealerInfo):
    dealerdb.insert_one(dict(dealer))
    return {"message": "Sucess", "code": 103}


@router.post("/checkdealer")
async def find_for_dealer(userid: Dealeruserid):
    checkdealer =  dealerdb.find_one(dict(userid))
    if (checkdealer):
        return {"dealer":str(checkdealer["_id"]),'code':104}
    else:
        return {"message":"Not sucess","code":105}

@router.get("/state")
async def state_dealer():
    state_data = statedb.find()
    return serializeList(state_data)

@router.get("/city")
async def city_dealer(stateid:str):
    city_data = citydb.find({"stateid":ObjectId(stateid)})
    return serializeLists(city_data)
    
