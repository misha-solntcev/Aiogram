""" Хэндлер для поиска контактов.
Инлайн клавиатура помещена тут-же потому что она использует
результаты запроса и формируется на лету.
Пользователь отправляет первые несолько символов,
и делается выборка записей из базы данных, содержающих эти
символы. Эти выбранные контакты прикрпляются к сообщению в виде
инлайн-кнопок. Далее user выбирает нужный контакт и в ответ получает
подробную информацию."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from DB.sqlite import Db


# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер реализует поиск контактов, срабатывает на любые сообщения и ищет в контактах.
@router.message()
async def search_conact(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True) )
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
        print(id, name)
        buttons.append(InlineKeyboardButton(text=f'\U0001F393  {name}', callback_data=id))
    keyb = kb_builder.add(*buttons).adjust(1).as_markup()

    if results:
        await message.answer(text=' \U0001F50E  Результаты поиска: ', reply_markup=keyb)
    else:
        await message.answer(text='Контакт не найден!')


db = Db()
query = db.search_all_id()
ids = [str(row[0]) for row in query]

# Обрабочик обратного вызова для выбранного контакта
@router.callback_query(F.data.in_(ids))
async def show_contact(callback: CallbackQuery):
    # print(callback.model_dump_json(indent=4, exclude_none=True))
    query = db.select_phonebook_id(callback.data)
    for item in query:
        await callback.message.answer(
            text=str(f' \U0001F393  <b>{item[0]}</b>\n\n'
                     f' \U0001F3DB  {item[2]}\n'
                     f' \U0001F454  {item[1]}\n\n'
                     f' \U0001F3DA  Кафедра: {item[3]}\n\n'
                     f' \U0001F4DE  tel: +7(3952)500-008 доб. {item[4]}\n\n'
                     f' \U0001F4E8  e-mail: {item[5]}'))
    await callback.answer()