from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_IDS, LOG_CHANNEL, PREMIUM_CHAT_ID
from database import add_user, set_premium, remove_premium, get_user, get_premium_users
import datetime


def premium_required(func):
    async def wrapper(client, message):
        user = await get_user(message.from_user.id)
        if not user or not user.get("premium"):
            return await message.reply("❌ You are not a premium user. Contact admin to subscribe.")
        return await func(client, message)
    return wrapper


def register_handlers(app: Client):

    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):
        await add_user(message.from_user.id)
        await message.reply("👋 Welcome! Use /buy to purchase premium.")

    @app.on_message(filters.command("buy"))
    async def buy_cmd(client, message):
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 Buy 1 Month – ₹100", callback_data="buy_1m")],
            [InlineKeyboardButton("💳 Buy 3 Months – ₹250", callback_data="buy_3m")],
        ])
        await message.reply("Select a plan:", reply_markup=kb)

    @app.on_callback_query(filters.regex(r"buy_"))
    async def buy_plan(client, query):
        plan = query.data
        duration = {"buy_1m": 30, "buy_3m": 90}[plan]
        expiry = datetime.datetime.now() + datetime.timedelta(days=duration)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"📝 {query.from_user.mention} requested {plan} plan."
            )
        await query.message.reply(
            f"Send payment screenshot to admin.\nPlan: {duration} days.\nExpiry: {expiry:%Y-%m-%d}"
        )

    # ✅ FIXED: Removed extra space before async def
    @app.on_message(filters.command("addpremium") & filters.user(ADMIN_IDS))
    async def add_premium_cmd(client, message):
        try:
            user_id = int(message.command[1])
            days = int(message.command[2])
        except:
            return await message.reply("Usage: /addpremium user_id days")

        expiry = datetime.datetime.now() + datetime.timedelta(days=days)
        await set_premium(user_id, expiry)

        # Try to add user to premium chat
        if PREMIUM_CHAT_ID:
            try:
                await client.add_chat_members(PREMIUM_CHAT_ID, user_id)
            except Exception as e:
                await message.reply(f"⚠️ Could not add user to premium chat: {e}")

        await message.reply(f"✅ Premium given to {user_id} for {days} days.")

    @app.on_message(filters.command("removepremium") & filters.user(ADMIN_IDS))
    async def remove_premium_cmd(client, message):
        try:
            user_id = int(message.command[1])
        except:
            return await message.reply("Usage: /removepremium user_id")

        await remove_premium(user_id)

        # Try to remove user from premium chat
        if PREMIUM_CHAT_ID:
            try:
                await client.ban_chat_member(PREMIUM_CHAT_ID, user_id)
                await client.unban_chat_member(PREMIUM_CHAT_ID, user_id)  # so they can rejoin later if renewed
            except Exception as e:
                await message.reply(f"⚠️ Could not remove user from premium chat: {e}")

        await message.reply(f"❌ Premium removed from {user_id}.")

    @app.on_message(filters.command("premiumlist") & filters.user(ADMIN_IDS))
    async def premium_list(client, message):
        text = "👑 Premium Users:\n"
        async for user in get_premium_users():
            text += f"- {user['user_id']} (Expiry: {user['expiry']})\n"
        await message.reply(text)
