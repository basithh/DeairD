from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from model.DealerModel import dealerdb, Dealeruserid, DealerInfo
from model.UserModel import userdb
from commonschema import serializeDict

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


