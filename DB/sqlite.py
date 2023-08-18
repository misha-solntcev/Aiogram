import sqlite3


# создаём класс для работы с базой данных
class Db:
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
        print('Database successfully connected...')

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

    # * Мой метод. Вывод всех уникальных дат
    def view_dates(self):
        # выбираем все уникальные даты
        self.cur.execute("SELECT DISTINCT date FROM shedule")
        dates = self.cur.fetchall()
        return dates

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

    # * Непонятный метод. // ищем запись по дате и выводим всю строку
    def search(self, date=""):
        # формируем запрос на поиск по точному совпадению
        self.cur.execute("SELECT * FROM shedule WHERE date=?", (date,))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows

    # * Мой метод. Ищем запись по дате и выводит строки без id и даты.
    def search_bydate(self, date=""):
        # формируем запрос на поиск по точному совпадению
        self.cur.execute("SELECT time, subject, lesson, location, teacher FROM shedule WHERE date=?", (date,))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows
