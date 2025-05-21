# main.py

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import database
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем токен и ID админа из .env
TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
# Потом исправим получение TOKEN и ADMIN_ID из env, а сейчас просто назначим здесь:
# ADMIN_ID = сюда можно вписать нужный ID для тестирования
# TOKEN = 'сюда можно вписать тестовый токен'

# Храним временные состояния пользователей
user_states = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Используйте /order для заказа или /review для отзыва.")


async def leave_review(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_states[user_id] = "awaiting_review"
    await update.message.reply_text("Пожалуйста, напишите ваш отзыв:")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_states.get(user_id) == "awaiting_review":
        username = update.effective_user.username or None
        database.save_review(user_id, username, text)
        await update.message.reply_text("Спасибо за ваш отзыв!")
        user_states[user_id] = None
    else:
        await update.message.reply_text("Я не ожидал сообщение от вас. Используйте команды.")


async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вы начали оформление заказа... (реализация здесь)")

async def admin_reviews(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Проверяем, является ли пользователь админом
    if user_id != ADMIN_ID:
        await update.message.reply_text("У вас нет доступа к этой команде.")
        return

    # Получаем все отзывы из БД
    reviews = database.get_all_reviews()

    if not reviews:
        await update.message.reply_text("Отзывов пока нет.")
        return

    # Формируем красивый вывод
    message = "📋 Все отзывы:\n\n"
    for review in reviews:
        _, user_id, username, text, created_at = review
        message += f"📅 {created_at}\n"
        message += f"👤 ID: {user_id}, @{username}\n"
        message += f"📝 Отзыв: {text}\n"
        message += "-" * 30 + "\n"

    # Если слишком длинное сообщение — разбиваем
    if len(message) > 4096:
        for chunk in [message[i:i+4096] for i in range(0, len(message), 4096)]:
            await update.message.reply_text(chunk)
    else:
        await update.message.reply_text(message)

def main():
    database.init_db()

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("review", leave_review))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("admin_reviews", admin_reviews))  # Новая команда

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()