from telebot import TeleBot
from keyboards.inline_keyboards import get_category_menu, get_dish_keyboard, get_continue_checkout
from repository.dish_repo import DishRepository
from models.dish import Dish

def register_handlers(bot: TeleBot):
    dish_repo = DishRepository(bot.get_dish_storage())

    @bot.message_handler(commands=['menu'])
    def show_categories(message):
        bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=get_category_menu())

    @bot.callback_query_handler(func=lambda call: call.data.startswith('category_'))
    def show_dishes_by_category(call):
        category_id = int(call.data.split('_')[1])
        dishes = dish_repo.get_by_category(category_id)

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
        dish = dish_repo.get_by_id(dish_id)
        if dish:
            bot.send_message(
                call.message.chat.id,
                f"<b>Подробное описание:</b>\n{dish.description}",
                parse_mode='HTML'
            )

    @bot.callback_query_handler(func=lambda call: call.data.startswith('add_'))
    def add_to_cart(call):
        dish_id = int(call.data.split('_')[1])
        dish = dish_repo.get_by_id(dish_id)

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