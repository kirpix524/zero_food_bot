import sqlite3

DB_NAME = 'bot.db'

def show_all_reviews():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reviews')
        reviews = cursor.fetchall()

        print("Все отзывы:")
        for review in reviews:
            print(review)

if __name__ == "__main__":
    show_all_reviews()