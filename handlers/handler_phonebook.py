from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from DB.sqlite import Db


# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на любые сообщения, реализует поиск контактов
@router.message()
async def search_conact(message: Message):
    search_term = message.text
    # Отправляем запрос к базе данных с использованием частичного соответствия
    db = Db()
    results = db.search_byname(search_term=search_term)
    # Создаем выпадающий список контактов с использованием ImlineKeyboardMarkup
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for i in range(len(results)):
        id = str(results[i][0])
        name = results[i][1]
        print(id, name, len(name.encode('utf-8')))
        buttons.append(InlineKeyboardButton(text=name, callback_data=id))
    keyb = kb_builder.add(*buttons).adjust(1).as_markup()

    if results:
        await message.answer(text='Результаты поиска: ', reply_markup=keyb)
    else:
        await message.answer(text='Контакт не найден!')

# # Обрабочик обратного вызова для выбранного контакта
# @router.callback_query(F.data.contains('show_contact:'))
# async def show_contact(callback: CallbackQuery):
#     name = callback.data.split(':')[1]
#     db = Db()
#     result = db.select_phonebook_name(name)
#     await callback.message.answer(result)
