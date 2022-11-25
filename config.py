#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5378430560:AAErIC7Bjr9MEVbzccnC9wm7BsLXfDtWhMM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "14712540"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e61b996dc037d969a4f8cf6411bb6165")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001614596050"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2009088107"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://BOTLOVER:BOTLOVER@cluster0.r4gz5oe.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001582946609"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "♥️ᴋᴏɴɪᴄʜɪᴡᴀ♥️ {first}\n\nɪ ᴀᴍ ᴀ 🧑‍💻🧑‍💻ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴛʜᴇ ɢʀᴇᴀᴛ ᴅᴇᴠɪʟs sᴏ ᴛʜᴇʏ ᴄᴀɴ ᴋᴇᴇᴘ ᴛʜᴇɪʀ ᴅᴀᴛᴀ ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇɪʀ ᴅᴀᴛᴀ ᴀs ᴀ ʟɪɴᴋ ᴛᴏ ᴀʟʟ ᴏᴛʜᴇʀ sᴜʙ ᴅᴇᴠɪʟs😜😜.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(2009088107)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
