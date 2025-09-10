from datetime import datetime, timedelta, timezone
from pyrogram.types import Message
from database import is_premium

# Timestamp helpers
def ts_now() -> int:
    return int(datetime.now(timezone.utc).timestamp())

def ts_after(days: int) -> int:
    return int((datetime.now(timezone.utc) + timedelta(days=days)).timestamp())

# Premium decorator
def premium_required(func):
    async def wrapper(client, message: Message):
        if await is_premium(message.from_user.id):
            return await func(client, message)
        else:
            return await message.reply_text("This command is for premium users only. Use /start to buy a plan.")
    return wrapper
