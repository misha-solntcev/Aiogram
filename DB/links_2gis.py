import sqlite3

db = sqlite3.connect('DB\db.db')
cur = db.cursor()
if cur:
    print("Соединение установлено успешно")

links = {
    1: "https://go.2gis.com/4b1xy",
    2: "https://go.2gis.com/ajr1y0",
    3: "https://go.2gis.com/xa4vb",
    4: "https://go.2gis.com/t4vtj",
    5: "https://go.2gis.com/2ayiu",
    6: "https://go.2gis.com/eawp54",
    7: "https://go.2gis.com/gl12bi",
    8: "https://go.2gis.com/vkjb4",
    9: "https://go.2gis.com/f7fhv",
    10:"https://go.2gis.com/lhg2v",
    11:"https://go.2gis.com/jhynf",
    12:"https://go.2gis.com/h5y0eo",
    13:"https://go.2gis.com/9m4s8"
}


# Создаем таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS gis
            (id, link)""")

# Записываем данные в БД
for key in links:
    cur.execute("INSERT INTO gis VALUES (?,?)",
        (key, links[key]))

db.commit()
db.close()
if not cur:
    print('Соединение закрыто')
