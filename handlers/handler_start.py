from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

# Хэндлер на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])