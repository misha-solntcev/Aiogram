import sqlite3 as sq
from config import Config, load_config

config: Config = load_config('.env')
db = sq.connect(config.db.database)
cur = db.cursor()
query = cur.execute("SELECT DISTINCT date FROM shedule").fetchall()
dates = [row[0] for row in query]

for date in dates:
    q = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (date,)).fetchall()
    print(date)
    for item in q:
        print(list(item))

db.close()
