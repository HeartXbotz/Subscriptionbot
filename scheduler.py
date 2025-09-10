import asyncio, datetime
from database import get_premium_users, remove_premium
from pyrogram import Client

async def expiry_checker(app: Client):
    while True:
        async for user in get_premium_users():
            if user["expiry"] and datetime.datetime.now() > user["expiry"]:
                await remove_premium(user["user_id"])
                try:
                    await app.send_message(user["user_id"], "⚠️ Your premium has expired.")
                except:
                    pass
        await asyncio.sleep(3600)  # check every hour
