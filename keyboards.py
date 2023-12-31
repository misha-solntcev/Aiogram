from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from DB.sqlite import Db


# Клавиатура с простыми кнопками для расписания лекций
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
# Загружаем список уникальных названий кнопок из базы данных
db = Db()
query = db.view_dates()
dates = [row[0] for row in query]
# Создаем список с кнопками
buttons: list[KeyboardButton] = [KeyboardButton(text=item) for item in dates]
# Распаковываем список с кнопками в билдер по 2 в ряд
kb_builder.add(*buttons).adjust(2)
keyboard = kb_builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите день")


# Инлайн-клавиатура ishedule
kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
# Загружаем список уникальных названий кнопок из базы данных
# и создаем список кнопок
buttons: list[InlineKeyboardButton] = []
db = Db()
query = db.view_dates()
dates = [row[0] for row in query]
for item in dates:
    buttons.append(InlineKeyboardButton(
        text=item,
        callback_data=item))
# Распаковываем список с кнопками в билдер по 2 в ряд
kb_builder.row(*buttons).adjust(2)
ikeyboard = kb_builder.as_markup()


# Инлайн-клавиатура ianswer. Кнопка со ссылкой формируется в зависимости
# от номера корпуса текущего запроса.
def get_kb_ianswer(num_build, teacher_id):
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    buttons.append(InlineKeyboardButton(text="\U00002139 инфо", callback_data=teacher_id))
    link = db.get_2gis_link(int(num_build))[0][0]
    buttons.append(InlineKeyboardButton(text="\U0001F4CD на карте", url= link))
    ianswer = kb_builder.add(*buttons).as_markup()
    return ianswer