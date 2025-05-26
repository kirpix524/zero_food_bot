from telebot import types

def get_dish_keyboard_with_add(dish_id):
    markup = types.InlineKeyboardMarkup()
    btn_details = types.InlineKeyboardButton("Подробнее", callback_data=f"details_{dish_id}")
    btn_add = types.InlineKeyboardButton("В корзину", callback_data=f"add_{dish_id}")
    markup.row(btn_details)
    markup.row(btn_add)
    return markup

def get_dish_keyboard(dish_id):
    markup = types.InlineKeyboardMarkup()
    btn_add = types.InlineKeyboardButton("В корзину", callback_data=f"add_{dish_id}")
    markup.row(btn_add)
    return markup

def get_continue_checkout():
    markup = types.InlineKeyboardMarkup()
    btn_continue = types.InlineKeyboardButton("Продолжить", callback_data="continue_shopping")
    btn_checkout = types.InlineKeyboardButton("Оформить заказ", callback_data="checkout")
    markup.row(btn_continue, btn_checkout)
    return markup

def select_payment_method_keyboard(order_id: int):
    markup = types.InlineKeyboardMarkup()
    btn_cash = types.InlineKeyboardButton("Наличные", callback_data=f"select_payment_cash:{order_id}")
    btn_card = types.InlineKeyboardButton("Карта", callback_data=f"select_payment_card:{order_id}")
    markup.row(btn_cash, btn_card)
    return markup