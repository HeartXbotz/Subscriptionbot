import asyncio
import logging
from datetime import datetime, timezone
from database import premium_col, purchase_col
from utils import ts_now

logger = logging.getLogger(name)

async def daily_maintenance(app):
    await app.wait_until_ready()
    logger.info("Background maintenance started")
    while True:
        try:
            now = ts_now()
            in_3_days_ts = now + 3 * 24 * 3600
            cursor = premium_col.find({"expiry_ts": {"$lte": in_3_days_ts, "$gt": now}})
            async for doc in cursor:
                uid = doc["user_id"]
                expiry_dt = datetime.fromtimestamp(doc["expiry_ts"], timezone.utc).isoformat()
                try:
                    await app.send_message(uid, f"Reminder: your premium expires on {expiry_dt} UTC.")
                except Exception:
                    pass

            await premium_col.delete_many({"expiry_ts": {"$lte": now}})
            week_ago = now - 7 * 24 * 3600
            await purchase_col.delete_many({"status": "pending", "created_at": {"$lte": week_ago}})
        except Exception as e:
            logger.exception("Error in maintenance loop: %s", e)
        await asyncio.sleep(24 * 3600)
