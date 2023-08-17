import sqlite3 as sq
from config import Config, load_config

config: Config = load_config('.env')

class SQLiteClient:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.con = sq.connect(config.db.database)

    def db_start():
        global db, cur
        db = sq.connect(config.db.database)
        cur = db.cursor()
        if db:
            print('Data base connected OK!')
        else:
            print('Data base connected failed!')
        cur.execute("""CREATE TABLE IF NOT EXISTS shedule
                (date, time, subject, lesson, location, teacher)""")
        db.commit()
