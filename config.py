import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# Multiple admin IDs separated by space
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split()))

# Optional log channel
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))

# Example: private group or channel where premium users are added
PREMIUM_CHAT_ID = int(os.getenv("PREMIUM_CHAT_ID", 0))
