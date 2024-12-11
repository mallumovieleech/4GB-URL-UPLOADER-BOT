import os
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from pyrogram import idle
from plugins.config import *





bot = Client(
    "url_uploader_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    sleep_threshold=250,
)

premium_client = Client(
    "premium_client",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.PREMIUM_SESSION_STRING,
    sleep_threshold=250,
)



# Start the bot
if __name__ == "__main__":
    bot.start()
    if premium_client:
        premium_client.start()
    idle()
    bot.stop()
    if premium_client:
        premium_client.stop()
