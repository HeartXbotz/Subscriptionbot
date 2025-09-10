import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("28455032"))
API_HASH = os.getenv("28dbb18229d7701a856c42a46083cccf")
BOT_TOKEN = os.getenv("7931356250:AAEl8s6RwaIh_Ek44u0-1JcX_lgthgITwCE")
MONGO_URI = os.getenv("mongodb+srv://kuttycloudbot:12@obitoleech.y3n6szj.mongodb.net/?retryWrites=true&w=majority&appName=Obitoleech")

# Multiple admin IDs separated by space
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "1572929036").split()))

# Optional log channel
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -1002463259408))

# Example: private group or channel where premium users are added
PREMIUM_CHAT_ID = int(os.getenv("PREMIUM_CHAT_ID", -1002854028155))
