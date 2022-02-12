from pydantic import BaseModel
from database import db

class UserModel(BaseModel):
    id: int
    username: str
    email: str
    phoneno: int
    password: str
    typeuser: str




userdb = db["user_db"]




