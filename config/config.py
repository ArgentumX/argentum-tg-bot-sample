import os

from dotenv import load_dotenv

USER_HELP = "❓Помощь"
CANCEL_STATE = "❌Отменить"

REFERER_ID_LEN = 20
load_dotenv()

# Throttling settings
DEFAULT_RATE_LIMIT = int(os.getenv("DEFAULT_RATE_LIMIT"))
DEFAULT_RATE_TIME_CYCLE = int(os.getenv("DEFAULT_RATE_TIME_CYCLE"))

# DB settings
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Other
ADMINS = eval(os.getenv("ADMINS"))
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ENABLE_DEVELOP_TOOLS = os.getenv("ENABLE_DEVELOP_TOOLS").lower() == "true"
MODERATOR_CONTACT = os.getenv("MODERATOR_CONTACT")
USER_AGREEMENT = os.getenv("USER_AGREEMENT")
BOT_LINK = os.getenv("BOT_LINK")
