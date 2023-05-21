import motor.motor_asyncio
from bson.objectid import ObjectId
from models.user_models import User
from models.event_models import Event


# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://simple:simple@cluster0.duulzju.mongodb.net/")


def UserHelper(User) -> dict:
    return {
        "_id": str(User["_id"]),
        "name": str(User["name"]),
        "email": str(User["email"]),
        "password": str(User["password"])
    }

def EventHelper(Event) -> dict:
    return{
        "_id": str(Event["_id"]),
        "host_id": str(Event["host_id"]),
        "name": str(Event["name"]),
        "open_date": str(Event["open_date"]),
        "close_date": str(Event["close_date"]), 
        "reward_box_id": str(Event["reward_box_id"])
    }

database = client.ProjectDatabase
collection_users = database.Users
collection_events = database.Events


async def register_user(user: User):
    result = await collection_users.insert_one(user)
    if result:
        registered_user = await collection_users.find_one(user)
        return UserHelper(registered_user)['_id']


async def login_user(email, password):
    result = await collection_users.find_one({"email": email, "password": password})
    if result:
        return UserHelper(result)["_id"]
    

async def deregister_user(user_id: ObjectId):
    document = user_id
    result = await collection_users.delete_one({"_id": ObjectId(user_id)})
    return document


async def create_event(event: Event):
    result = await collection_events.insert_one(event)
    if result:
        registered_event = await collection_events.find_one(event)
        return EventHelper(registered_event)['_id']