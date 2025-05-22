from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.bot import ZeroFoodBot
from builders.category_builder import CategoryMenuBuilder

# Храним временные состояния пользователей
user_states = {}

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

    # Запрос отзыва
    @bot.bot.message_handler(commands=['review'])
    def leave_review(message: types.Message) -> None:
        user_id = message.from_user.id
        user_states[user_id] = "awaiting_review"
        bot.bot.send_message(message.chat.id, "Пожалуйста, напишите ваш отзыв:")

    # Получение отзыва, обработка отзыва и запись отзыва в базу отзывов
    @bot.bot.message_handler(content_types=['text'])
    def handle_message(message: types.Message) -> None:
        user_id = message.from_user.id
        text = message.text

        if user_states.get(user_id) == "awaiting_review":
            username = message.from_user.username or "Без ника"
            from database import save_review
            save_review(user_id, username, text)
            bot.bot.send_message(message.chat.id, "Спасибо за ваш отзыв!")
            user_states[user_id] = None
        else:
            bot.bot.send_message(message.chat.id, "Я не ожидал сообщение от вас. Используйте команды.")

    # Функция админа - вывод всех отзывов
    @bot.bot.message_handler(commands=['admin_reviews'])
    def admin_reviews(message: types.Message) -> None:
        from config import ADMIN_ID
        from database import get_all_reviews

        user_id = message.from_user.id

        if user_id != ADMIN_ID:
            bot.bot.send_message(message.chat.id, "У вас нет доступа к этой команде.")
            return

        reviews = get_all_reviews()

        if not reviews:
            bot.bot.send_message(message.chat.id, "Отзывов пока нет.")
            return

        message_text = "📋 Все отзывы:\n\n"
        for review in reviews:
            _, user_id, username, text, created_at = review
            message_text += f"📅 {created_at}\n"
            message_text += f"👤 ID: {user_id}, @{username}\n"
            message_text += f"📝 Отзыв: {text}\n"
            message_text += "-" * 30 + "\n"

        # Разбиваем на части, если слишком длинное
        max_length = 4096
        for i in range(0, len(message_text), max_length):
            chunk = message_text[i:i + max_length]
            bot.bot.send_message(message.chat.id, chunk)
        bot.answer_callback_query(callback_query_id=callback_query.id, text=response_text)
