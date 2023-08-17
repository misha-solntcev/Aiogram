# Рабочий асинхронный вариант запуска парсинга
# Функция Foo() запускается с определенным интервалом

import asyncio
from asyncio import Task
import logging
from aiogram import Bot, Dispatcher
from config import Config, load_config
from handlers import handler_start, handler_other, handler_shedule, handler_game

# Инициализируем логгер
logger = logging.getLogger(__name__)

async def Foo():
    while True:
        print("Я асинхронная функция")
        await asyncio.sleep(3)

# Функция конфигурирования и запуска бота
async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')

    config = load_config('.env')
    bot: Bot = Bot(config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(handler_start.router)
    dp.include_router(handler_shedule.router)
    dp.include_router(handler_game.router)
    # dp.include_router(handler_other.router)

    task: Task = asyncio.create_task(Foo())

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await task

if __name__ == '__main__':
    asyncio.run(main())
