import code
from fastapi import APIRouter
from model.UserModel import UserModel, userdb




router = APIRouter()


@router.post("/register")
async def register_user(user: UserModel):
    id = userdb.insert_one(dict(user))
    usercheck = userdb.find_one({"_id": id.inserted_id})
    return {
                "message": "Sucess",
                "code": 100,
                "userid": str(usercheck["_id"]),
                "username": usercheck["username"],
                "typeuser": usercheck["typeuser"]
            }


@router.post("/login")
async def login_user(email: str, password: str):
    usercheck = userdb.find_one({"email": email})
    if(usercheck):
        if (usercheck["password"] == password):
            return {
                "message": "Sucess",
                "code": 100,
                "userid": str(usercheck["_id"]),
                "typeuser": usercheck["typeuser"]
            }
        else:
            return {"message": "Password Wrong", "code": 101}
    else:
        return {"message": "User not found", "code": 102}
