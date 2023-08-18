from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards import shed_kb
import sqlite3 as sq
from config import Config, load_config

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /shedule
@router.message(Command(commands=['shedule']))
async def process_button_command(message: Message):
    await message.answer(text='Ловите расписание лекций', reply_markup=shed_kb)


config: Config = load_config('.env')
db = sq.connect(config.db.database)
cur = db.cursor()
query = cur.execute("SELECT DISTINCT date FROM shedule").fetchall()
dates = [row[0] for row in query]
db.close()

@router.message(F.text == dates[0])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[0],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[1])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[1],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[2])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[2],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[3])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[3],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[4])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[4],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[5])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[5],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[6])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[6],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[7])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[7],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[8])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[8],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[9])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[9],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[10])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[10],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[11])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[11],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[12])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[12],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[13])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[13],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[14])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[14],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[15])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[15],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[16])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[16],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))

@router.message(F.text == dates[17])
async def process_reply_command(message: Message):
    config: Config = load_config('.env')
    db = sq.connect(config.db.database)
    cur = db.cursor()
    query = cur.execute(f"SELECT time, subject, lesson, location, teacher FROM shedule WHERE date = ?", (dates[17],)).fetchall()
    db.close()
    for item in query:
        await message.answer(text=str(item))