from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import keyboard, get_kb_ianswer
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

@router.message(F.text.in_(dates))
async def process_reply_command(message: Message):
    query = db.search_bydate(message.text)
    for item in query:
        # Получаем номер корпуса из базы данных (отделяем корпус от аудитории)
        num_build = item[3].split('-')[0]
        # Получаем id преподователя для callback. Если такого нет, то
        # читаем id 1000, там запись "Нет данных".
        try:
            teacher_id = str(db.get_teacher_id(item[4])[0][0])
        except Exception as e:
            print(e)
            teacher_id = "1000"
        await message.answer(
            text=str(f' \U0001F558  <b>{item[0]}</b>\n'
                    f' \U0001F4DA  {item[1]}\n'
                    f' \U0001F4D6  {item[2]}\n'
                    f' \U0001F3DA  {item[3]}\n'
                    f' \U0001F393  <b>{item[4]}</b>'
                    ), reply_markup=get_kb_ianswer(num_build, teacher_id))
