import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split()))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))

PLANS = {
    "1 Month": {"days": 30, "price": "₹99"},
    "3 Months": {"days": 90, "price": "₹249"},
    "6 Months": {"days": 180, "price": "₹399"},
}
