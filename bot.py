import asyncio
import logging

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import register_handlers
from scheduler import daily_maintenance

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

app = Client("subscription-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    register_handlers(app)
    asyncio.create_task(daily_maintenance(app))
    await app.start()
    logger.info("Bot started")
    await app.idle()

if name == "main":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
