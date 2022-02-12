from pydantic import BaseModel
from database import db

class UserModel(BaseModel):
    username: str
    email: str
    phoneno: str
    password: str
    typeuser: str

userdb = db["user_db"]




