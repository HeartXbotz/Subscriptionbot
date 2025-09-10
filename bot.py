import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from scheduler import expiry_checker

# 🔹 Create bot client
app = Client(
    "subscription_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# 🔹 Register message/command handlers
register_handlers(app)

async def main():
    await app.start()
    asyncio.create_task(expiry_checker(app))  # background expiry check
    print("🤖 Subscription Bot Started.")
    await asyncio.Event().wait()  # keep running

if __name__ == "__main__":
    asyncio.run(main())
