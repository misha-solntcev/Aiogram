import sqlite3

# Соединяемся с БД (Если ее нет, то будет создана)
db = sqlite3.connect('zis.db')

# Создаем курсор
cursor = db.cursor()

# # Создаем таблицу
# cursor.execute("""CREATE TABLE articles (
#           title text,
#           full_text text,
#           views integer,
#           author text 
# ) """)

# Добавление данных
# cursor.execute("""INSERT INTO articles VALUES(
#                'Yandex is cool!',
#                'Yandex is really cool!',
#                200,
#                'Admin'
#                )""")

# # Удаление данных
# cursor.execute("DELETE FROM articles WHERE author = 'Admin'")

# Обновление данных
cursor.execute("UPDATE articles SET views = 777, author = 'Putin' WHERE title = 'Goolge is cool!'")

# Выборка данных
cursor.execute("SELECT rowid, * FROM articles WHERE rowid <= 4")
# print(cursor.fetchall())
# print(cursor.fetchmany(1))
# print(cursor.fetchone())
# print(cursor.fetchone()[1])

items = cursor.fetchall()
for item in items:
    print(item)


db.commit()

db.close()

