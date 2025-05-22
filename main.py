from app.bot import ZeroFoodBot
from app.init_repositories import init_repositories
from app.init_storage import init_storage
from handlers import init_handlers
from config import TG_API_KEY
from log_funcs import logger
from storage.db_session import DBSession
from config import SQL_DATA

db_session = DBSession(SQL_DATA["db_path"])

bot=ZeroFoodBot(TG_API_KEY)
storage_list = init_storage(db_session)
init_repositories(bot, storage_list)
init_handlers(bot)

print("bot is running")
logger.info("bot is running")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
