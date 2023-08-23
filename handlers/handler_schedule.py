from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards import keyboard
from DB.sqlite import Db

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /shedule
@router.message(Command(commands=['schedule']))
async def process_button_command(message: Message):
    await message.answer(text='Расписание лекций', reply_markup=keyboard)

db = Db()
query = db.view_dates()
dates = [row[0] for row in query]

# Инлайн-клавиатура ianswer. Кнопка со ссылкой формируется в зависимости
# от номера корпуса текущего запроса.
def get_kb_ianswer(num_build, teacher):
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    buttons.append(InlineKeyboardButton(text="\U00002139 инфо", callback_data="info"))
    link = db.get_2gis_link(int(num_build))[0][0]
    buttons.append(InlineKeyboardButton(text="\U0001F4CD на карте", url= link))
    ianswer = kb_builder.add(*buttons).as_markup()
    return ianswer


@router.message(F.text == dates[0])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[0])
    for item in query:
        num_build = item[3].split('-')[0] # Получаем номер корпуса из базы данных
        await message.answer(
            text=str(f' \U0001F558  <b>{item[0]}</b>\n\n'
                     f' \U0001F4DA  {item[1]}\n'
                     f' \U0001F4D6  {item[2]}\n'
                     f' \U0001F3DA  {item[3]}\n\n'
                     f' \U0001F393  <b>{item[4]}</b>\n\n'
                     ), reply_markup=get_kb_ianswer(num_build))

@router.message(F.text == dates[1])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[1])
    for item in query:
        num_build = item[3].split('-')[0] # Получаем номер корпуса из базы данных
        await message.answer(
            text=str(f' \U0001F558  <b>{item[0]}</b>\n\n'
                     f' \U0001F4DA  {item[1]}\n'
                     f' \U0001F4D6  {item[2]}\n'
                     f' \U0001F3DA  {item[3]}\n\n'
                     f' \U0001F393  <b>{item[4]}</b>\n\n'
                     ), reply_markup=get_kb_ianswer(num_build))

@router.message(F.text == dates[2])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[2])
    for item in query:
        num_build = item[3].split('-')[0] # Получаем номер корпуса из базы данных
        await message.answer(
            text=str(f' \U0001F558  <b>{item[0]}</b>\n\n'
                     f' \U0001F4DA  {item[1]}\n'
                     f' \U0001F4D6  {item[2]}\n'
                     f' \U0001F3DA  {item[3]}\n\n'
                     f' \U0001F393  <b>{item[4]}</b>\n\n'
                     ), reply_markup=get_kb_ianswer(num_build))

@router.message(F.text == dates[3])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[3])
    for item in query:
        num_build = item[3].split('-')[0] # Получаем номер корпуса из базы данных
        await message.answer(
            text=str(f' \U0001F558  <b>{item[0]}</b>\n\n'
                     f' \U0001F4DA  {item[1]}\n'
                     f' \U0001F4D6  {item[2]}\n'
                     f' \U0001F3DA  {item[3]}\n\n'
                     f' \U0001F393  <b>{item[4]}</b>\n\n'
                     ), reply_markup=get_kb_ianswer(num_build))

@router.message(F.text == dates[4])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[4])
    for item in query:
        num_build = item[3].split('-')[0] # Получаем номер корпуса из базы данных
        await message.answer(
            text=str(f' \U0001F558  <b>{item[0]}</b>\n\n'
                     f' \U0001F4DA  {item[1]}\n'
                     f' \U0001F4D6  {item[2]}\n'
                     f' \U0001F3DA  {item[3]}\n\n'
                     f' \U0001F393  <b>{item[4]}</b>\n\n'
                     ), reply_markup=get_kb_ianswer(num_build))

@router.message(F.text == dates[5])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[5])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[6])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[6])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[7])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[7])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[8])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[8])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[9])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[9])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[10])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[10])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[11])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[11])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[12])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[12])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[13])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[13])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[14])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[14])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[15])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[15])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[16])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[16])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[17])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[17])
    for item in query:
        await message.answer(text=str(item))