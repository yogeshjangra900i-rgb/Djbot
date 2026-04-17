

from os import environ

API_ID = int(environ.get("30296254", ""))
API_HASH = environ.get("c2b5306f4ccd2d795405a026c10b4c62", "")
BOT_TOKEN = environ.get("8729794086:AAGImqYUrPm86zftTZ1Q9-JK09FhGOf8ymo", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/bot_subscription")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("7660916897", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





