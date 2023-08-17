from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import game_kb, yes_no_kb
from lexicon import LEXICON_RU
from services import get_bot_choice, get_winner

# Инициализируем роутер уровня модуля
router: Router = Router()

# Хэндлер на команду /game
@router.message(Command(commands=['game']))
async def process_game_command(message: Message):
    await message.answer(text=LEXICON_RU['/game'], reply_markup=yes_no_kb)

# Хэндлер на команду /helpgame
@router.message(Command(commands=['helpgame']))
async def process_helpgame_command(message: Message):
    await message.answer(text=LEXICON_RU['/helpgame'], reply_markup=yes_no_kb)

# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(F.text.in_([LEXICON_RU['rock'],
                           LEXICON_RU['paper'],
                           LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
