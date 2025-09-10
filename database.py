from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI
from utils import ts_now, ts_after

mongo = AsyncIOMotorClient(MONGO_URI)
db = mongo["subscription_bot"]
premium_col = db["premiums"]
purchase_col = db["purchases"]

async def add_premium(user_id: int, days: int, plan_name: str = None):
    now = ts_now()
    existing = await premium_col.find_one({"user_id": user_id})
    if existing and existing.get("expiry_ts", 0) > now:
        new_expiry = existing["expiry_ts"] + days * 24 * 3600
    else:
        new_expiry = ts_after(days)
    doc = {
        "user_id": user_id,
        "expiry_ts": new_expiry,
        "plan": plan_name or f"{days}d",
        "updated_at": now,
    }
    await premium_col.update_one({"user_id": user_id}, {"$set": doc}, upsert=True)
    return new_expiry

async def remove_premium(user_id: int):
    await premium_col.delete_one({"user_id": user_id})

async def is_premium(user_id: int) -> bool:
    now = ts_now()
    doc = await premium_col.find_one({"user_id": user_id})
    return bool(doc and doc.get("expiry_ts", 0) > now)

async def get_premium_list(limit: int = 100):
    cursor = premium_col.find().sort("expiry_ts", 1).limit(limit)
    return await cursor.to_list(length=limit)
