from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.bot import ZeroFoodBot
from builders.category_builder import CategoryMenuBuilder



def init_handlers(bot: ZeroFoodBot) -> None:
    category_repository = bot.get_category_repository()
    builder = CategoryMenuBuilder(category_repository)

    @bot.message_handler(commands=['menu'])
    def cmd_categories(message: types.Message) -> None:
        markup: InlineKeyboardMarkup = builder.build_menu()
        bot.send_message(chat_id=message.chat.id, text="Пожалуйста, выберите категорию:", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("category_select:"))
    def process_category(callback_query: types.CallbackQuery) -> None:
        category_id: int = int(callback_query.data.split(":", 1)[1])
        category = category_repository.get_by_id(category_id)
        if category:
            response_text: str = f"Вы выбрали категорию «{category.name}»"
        else:
            response_text: str = "Категория не найдена"
        bot.answer_callback_query(callback_query_id=callback_query.id, text=response_text)