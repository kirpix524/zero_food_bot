from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.bot import ZeroFoodBot
from builders.main_menu_builder import MainMenuBuilder
from keyboards.inline_keyboards import get_dish_keyboard, get_continue_checkout

# Храним временные состояния пользователей
user_states = {}

def init_handlers(bot: ZeroFoodBot) -> None:
    def show_categories(message: types.Message) -> None:
        if not bot.category_menu_builder:
            bot.send_message(chat_id=message.chat.id, text="Категории не загружены")
            return
        markup: InlineKeyboardMarkup = bot.category_menu_builder.build_menu()
        bot.send_message(chat_id=message.chat.id, text="Пожалуйста, выберите категорию:", reply_markup=markup)

    #отображение главного меню
    @bot.message_handler(commands=['start'])
    def cmd_start(message: types.Message) -> None:
        markup = MainMenuBuilder.build_menu(message.from_user.id)
        bot.send_message(chat_id=message.chat.id, text="Выберите действие:", reply_markup=markup)

    #отображение категорий меню
    @bot.message_handler(commands=['show_menu'])
    def cmd_categories(message: types.Message) -> None:
        show_categories(message)

    @bot.callback_query_handler(func=lambda call: call.data and call.data.startswith("category_select:"))
    def process_category(callback_query: types.CallbackQuery) -> None:
        category_id: int = int(callback_query.data.split(":", 1)[1])
        category = bot.get_category_repository().get_by_id(category_id)
        if category:
            response_text: str = f"Вы выбрали категорию «{category.name}»"
        else:
            response_text: str = "Категория не найдена"
        bot.answer_callback_query(callback_query_id=callback_query.id, text=response_text)

    #отображение заказов
    @bot.message_handler(commands=['show_orders'])
    def show_orders(message: types.Message) -> None:
        pass



    @bot.callback_query_handler(func=lambda call: call.data.startswith('category_'))
    def show_dishes_by_category(call):
        category_id = int(call.data.split('_')[1])
        dishes = bot.get_dish_repository().get_by_category(category_id)

        if not dishes:
            bot.send_message(call.message.chat.id, "Блюда не найдены.")
            return

        for dish in dishes:
            try:
                with open(dish.photo_url, 'rb') as photo:
                    bot.send_photo(
                        chat_id=call.message.chat.id,
                        photo=photo,
                        caption=f"<b>{dish.name}</b>\n{dish.short_description}\n\nЦена: {dish.price} ₽",
                        parse_mode='HTML',
                        reply_markup=get_dish_keyboard(dish.id)
                    )
            except Exception as e:
                bot.send_message(call.message.chat.id, f"Ошибка при отображении {dish.name}: {e}")

    @bot.callback_query_handler(func=lambda call: call.data.startswith('details_'))
    def show_dish_details(call):
        dish_id = int(call.data.split('_')[1])
        dish = bot.get_dish_repository().get_by_id(dish_id)
        if dish:
            bot.send_message(
                call.message.chat.id,
                f"<b>Подробное описание:</b>\n{dish.description}",
                parse_mode='HTML'
            )

    @bot.callback_query_handler(func=lambda call: call.data.startswith('add_'))
    def add_to_cart(call):
        dish_id = int(call.data.split('_')[1])
        dish = bot.get_dish_repository().get_by_id(dish_id)

        msg = bot.send_message(
            call.message.chat.id,
            f"Введите количество для '{dish.name}':"
        )
        bot.register_next_step_handler(msg, lambda m: ask_quantity(m, dish))

    def ask_quantity(message, dish):
        try:
            quantity = int(message.text)
            total_price = dish.price * quantity
            bot.send_message(
                message.chat.id,
                f"Добавлено в корзину:\n{dish.name} x{quantity}\nИтого: {total_price} ₽",
                reply_markup=get_continue_checkout()
            )
        except ValueError:
            bot.send_message(message.chat.id, "Введите число!")
            bot.register_next_step_handler(message, lambda m: ask_quantity(m, dish))

    @bot.callback_query_handler(func=lambda call: call.data == 'continue_shopping')
    def continue_shopping(call):
        show_categories(call.message)

    @bot.callback_query_handler(func=lambda call: call.data == 'checkout')
    def checkout_order(call):
        bot.send_message(call.message.chat.id, "Ваш заказ оформлен! Ожидайте.")


    # Запрос отзыва
    @bot.message_handler(commands=['add_feedback'])
    def leave_review(message: types.Message) -> None:
        user_id = message.from_user.id
        user_states[user_id] = "awaiting_review"
        bot.send_message(message.chat.id, "Пожалуйста, напишите ваш отзыв:")

    # Получение отзыва, обработка отзыва и запись отзыва в базу отзывов
    @bot.message_handler(content_types=['text'])
    def handle_message(message: types.Message) -> None:
        user_id = message.from_user.id
        text = message.text

        if user_states.get(user_id) == "awaiting_review":
            username = message.from_user.username or "Без ника"
            from database import save_review
            save_review(user_id, username, text)
            bot.send_message(message.chat.id, "Спасибо за ваш отзыв!")
            user_states[user_id] = None
        else:
            bot.send_message(message.chat.id, "Я не ожидал сообщение от вас. Используйте команды.")

    # Функция админа - вывод всех отзывов
    @bot.message_handler(commands=['admin_reviews'])
    def admin_reviews(message: types.Message) -> None:
        from config import ADMINS
        from database import get_all_reviews

        user_id = message.from_user.id

        if user_id not in ADMINS:
            bot.send_message(message.chat.id, "У вас нет доступа к этой команде.")
            return

        reviews = bot.get_feedback_repository().get_all()

        if not reviews:
            bot.send_message(message.chat.id, "Отзывов пока нет.")
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
            bot.send_message(message.chat.id, chunk)
