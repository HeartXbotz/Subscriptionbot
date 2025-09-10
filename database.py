import motor.motor_asyncio
from config import MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.subscription_bot

users_col = db.users
subs_col = db.subscriptions

async def add_user(user_id: int):
    if not await users_col.find_one({"user_id": user_id}):
        await users_col.insert_one({"user_id": user_id, "premium": False, "expiry": None})

async def set_premium(user_id: int, expiry):
    await users_col.update_one(
        {"user_id": user_id},
        {"$set": {"premium": True, "expiry": expiry}},
        upsert=True
    )

async def remove_premium(user_id: int):
    await users_col.update_one(
        {"user_id": user_id},
        {"$set": {"premium": False, "expiry": None}}
    )

async def get_user(user_id: int):
    return await users_col.find_one({"user_id": user_id})

async def get_premium_users():
    return users_col.find({"premium": True})
