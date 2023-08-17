import sqlite3 as sq
from config import Config, load_config


config: Config = load_config('F:\Файлы\Aiogram\.env')
db = sq.connect(config.db.database)
cur = db.cursor()
lst = list(cur.execute("""SELECT date FROM shedule"""))
db.commit()
db.close()

print(lst, type(lst))