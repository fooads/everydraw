from pydantic import BaseModel
from bson.objectid import ObjectId

class User(BaseModel):
    _id: ObjectId
    name: str
    email: str
    password: str


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserId(BaseModel):
    user_id: str