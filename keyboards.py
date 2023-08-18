from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import Config, load_config
from DB.sqlite import Db


# Создаем клавиатуру для расписания лекций
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем список уникальных названий кнопок
db = Db()
query = db.view_dates()
dates = [row[0] for row in query]

# Создаем список с кнопками
buttons: list[KeyboardButton] = [KeyboardButton(text=item) for item in dates]

# Распаковываем список с кнопками в билдер по 2 в ряд
kb_builder.add(*buttons).adjust(2)

shed_kb = kb_builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите день недели")
