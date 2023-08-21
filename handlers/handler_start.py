from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text="Привет! Я бот помощник. Выбери в меню 'Расписание занятий' или набери команду /schedule, выбери день, и я напишу тебе расписание на этот день.")

# Хэндлер на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text="Тут должна быть справка.")