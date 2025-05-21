import telebot
from config import TG_API_KEY
from log_funcs import logger

bot=telebot.TeleBot(TG_API_KEY)

print("bot is running")
logger.info("bot is running")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
