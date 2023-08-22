from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards import ikeyboard
from DB.sqlite import Db

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /ishedule
@router.message(Command(commands=['ischedule']))
async def handler(message: Message):
    await message.answer(text='i Расписание', reply_markup=ikeyboard)

db = Db()
query = db.view_dates()
dates = [row[0] for row in query]

# Хэндлер на update типа CallbackQuery
@router.callback_query(F.data.in_(dates))
async def ibtn(callback: CallbackQuery):
    await callback.message.answer(f"&#8987<pre>{callback.data}</pre>&#8987")
    query = db.search_bydate(callback.data)
    for item in query:
        await callback.message.answer(str(item))
    await callback.answer()
