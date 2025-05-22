# database.py
# import sqlite3
#
# DB_NAME = 'bot.db'
#
# def init_db():
#     with sqlite3.connect(DB_NAME) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS reviews (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER NOT NULL,
#                 username TEXT,
#                 review_text TEXT NOT NULL,
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         ''')
#         conn.commit()
#
# def save_review(user_id, username, text):
#     with sqlite3.connect(DB_NAME) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO reviews (user_id, username, review_text)
#             VALUES (?, ?, ?)
#         ''', (user_id, username, text))
#         conn.commit()
#
# def get_all_reviews():
#     with sqlite3.connect(DB_NAME) as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM reviews ORDER BY created_at DESC")
#         return cursor.fetchall()