import os
from dotenv import load_dotenv

load_dotenv()  # loads from .env file if exists

API_ID = int(os.getenv("API_ID", "28455032"))
API_HASH = os.getenv("API_HASH", "28dbb18229d7701a856c42a46083cccf")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7931356250:AAEl8s6RwaIh_Ek44u0-1JcX_lgthgITwCE")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://kuttycloudbot:12@obitoleech.y3n6szj.mongodb.net/?retryWrites=true&w=majority&appName=Obitoleech")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "1572929036").split()))
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002463259408"))
