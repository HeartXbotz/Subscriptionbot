import asyncio, datetime
from database import get_premium_users, remove_premium
from pyrogram import Client
from config import PREMIUM_CHAT_ID

async def expiry_checker(app: Client):
    while True:
        async for user in get_premium_users():
            if user["expiry"] and datetime.datetime.now() > user["expiry"]:
                await remove_premium(user["user_id"])
                try:
                    if PREMIUM_CHAT_ID:
                        await app.ban_chat_member(PREMIUM_CHAT_ID, user["user_id"])
                        await app.unban_chat_member(PREMIUM_CHAT_ID, user["user_id"])
                    await app.send_message(user["user_id"], "⚠️ Your premium has expired and you have been removed from the premium chat.")
                except:
                    pass
        await asyncio.sleep(3600)



