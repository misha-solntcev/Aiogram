from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon import LEXICON_RU

# Создаем клавиатуру для расписания лекций"
# Инициализируем builder
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Создаем список названий кнопок
lst = ['13 марта 2023 г. (Понедельник)', '14 марта 2023 г. (Вторник)',
       '15 марта 2023 г. (Среда)', '16 марта 2023 г. (Четверг)',
       '17 марта 2023 г. (Пятница)', '18 марта 2023 г. (Суббота)',
       '20 марта 2023 г. (Понедельник)', '21 марта 2023 г. (Вторник)',
       '22 марта 2023 г. (Среда)', '23 марта 2023 г. (Четверг)',
       '24 марта 2023 г. (Пятница)', '25 марта 2023 г. (Суббота)',
       '27 марта 2023 г. (Понедельник)', '28 марта 2023 г. (Вторник)',
       '29 марта 2023 г. (Среда)','30 марта 2023 г. (Четверг)',
       '31 марта 2023 г. (Пятница)', '1 апреля 2023 г. (Суббота)']
# Создаем список с кнопками
buttons: list[KeyboardButton] = [KeyboardButton(text=i) for i in lst]
# Распаковываем список с кнопками в билдер по 2 в ряд
kb_builder.add(*buttons).adjust(2)
shed_kb = kb_builder.as_markup(resize_keyboard=True,
        input_field_placeholder="Выберите день недели")
