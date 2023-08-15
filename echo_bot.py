from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

TOKEN: str = "6279685448:AAGU22Rs1BEKA4bEZMoOL80JY05C_ayITWw"

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Привет\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь")

# Хэндлер на команду /help
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("Напиши мне что-нибудь и в ответ "
                         "я пришлю тебе твое сообщение")

# Эхо хэндлер на фото
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')

# # Эхо хэндлер на любой текст
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)