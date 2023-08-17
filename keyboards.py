from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import sqlite3 as sq
from config import Config, load_config


# Создаем клавиатуру для расписания лекций"
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем список названий кнопок

config: Config = load_config('.env')
db = sq.connect(config.db.database)
cur = db.cursor()
query = cur.execute("SELECT DISTINCT date FROM shedule").fetchall()
date = [row[0] for row in query]
db.close()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [KeyboardButton(text=item) for item in date]
# Распаковываем список с кнопками в билдер по 2 в ряд
kb_builder.add(*buttons).adjust(2)

shed_kb = kb_builder.as_markup(resize_keyboard=True,
        input_field_placeholder="Выберите день недели")
