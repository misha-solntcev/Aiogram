from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards import shed_kb
from DB.sqlite import Db

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /shedule
@router.message(Command(commands=['shedule']))
async def process_button_command(message: Message):
    await message.answer(text='Ловите расписание лекций', reply_markup=shed_kb)

db = Db()
query = db.view_dates()
dates = [row[0] for row in query]

@router.message(F.text == dates[0])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[0])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[1])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[1])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[2])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[2])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[3])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[3])
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[4])
async def process_reply_command(message: Message):
    query = db.search_bydate(dates[4])
    for item in query:
        await message.answer(text=str(item))

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
