import sqlite3
# from config import Config, load_config
# config: Config = load_config('.env')


# создаём класс для работы с базой данных
class DB:
    # конструктор класса
    def __init__(self):
        # соединяемся с файлом базы данных
        self.conn = sqlite3.connect("DB\db.db")
        # создаём курсор для виртуального управления базой данных
        self.cur = self.conn.cursor()
        # если нужной нам таблицы в базе нет — создаём её
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS shedule (id INTEGER PRIMARY KEY, date, time, subject, lesson, location, teacher)")
        # сохраняем сделанные изменения в базе
        self.conn.commit()

    # деструктор класса
    def __del__(self):
        # отключаемся от базы при завершении работы
        self.conn.close()

    # просмотр всех записей
    def view(self):
        # выбираем все записи расписания
        self.cur.execute("SELECT * FROM shedule")
        # собираем все найденные записи в колонку со строками
        rows = self.cur.fetchall()
        # возвращаем сроки с записями расходов
        return rows

    # добавляем новую запись
    def insert(self, date, time, subject, lesson, location, teacher):
        # формируем запрос с добавлением новой записи в БД
        self.cur.execute("INSERT INTO shedule VALUES (NULL,?,?,?,?,?,?)", (date, time, subject, lesson, location, teacher,))
        # сохраняем изменения
        self.conn.commit()


    # обновляем информацию о расписании
    def update(self, id, date, time, subject, lesson, location, teacher):
        # формируем запрос на обновление записи в БД
        self.cur.execute("UPDATE shedule SET date=?, time=?, subject=?, lesson=?, location=?, teacher=? WHERE id=?", (date, time, subject, lesson, location, teacher, id,))
        # сохраняем изменения
        self.conn.commit()

    # удаляем запись
    def delete(self, id):
        # формируем запрос на удаление записи по id
        self.cur.execute("DELETE FROM shedule WHERE id=?", (id,))
        # сохраняем изменения
        self.conn.commit()

    # ищем запись по дате
    def search(self, date="", price=""):
        # формируем запрос на поиск по точному совпадению
        self.cur.execute("SELECT * FROM shedule WHERE date=?", (date,))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows

# создаём экземпляр базы данных на основе класса
db = DB()

print(db.view())