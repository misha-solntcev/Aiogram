from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboards import shed_kb

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /shedule
@router.message(Command(commands=['shedule']))
async def process_button_command(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer(text='Ловите расписание лекций',
        reply_markup=shed_kb)

# Хэндлер на '13 марта 2023 г. (Понедельник)'
@router.message(F.text == '13 марта 2023 г. (Понедельник)')
async def process_reply_command(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply(text="Это расписание на '13 марта 2023 г. (Понедельник)'",
        reply_markup=shed_kb)
