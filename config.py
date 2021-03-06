
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1519216560:AAGRSfI2uHWT_JRxCSTE2mAB-zEa-TIO9E4")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "1479154"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "6b21cb22818e09132fb904705c31d3a1")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAtL16QJn_nd2Nco2VsOrN57_mrP5vcO7mTMHh2d2UL6k-FET-w5V03AwlJsjToDovDqZxMqmR-bmpFJYw9AD_mED3eTIV3ZTZ49547Dv8zHo4OTdFMkF3J8WGZQFUQ0PfpEjZ9qR9n5m_L-yiaaPj5gWKOfrKeAf_rtIL0AWhkvk_V1uvlpABgLd1QJD-tGbF41ezrwi5-2NhQYUDkEGqlHBwT7uvPheIiNC1RK1n60dl62P5oJ5CzCVElrAOUgWnqxRI3B_rB7PDGg8bGp2QKvFBSSLcFGBLCxAUmESLGn8JCdN0dcaIkku8g9AAMzo5FzbCbk_gvScyrcgkzGBFFK1W33QA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001433161521")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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
