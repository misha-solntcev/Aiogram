import asyncio
from aiogram import Bot, Dispatcher
from config import Config, load_config
import user_handlers, other_handlers

# Функция конфигурирования и запуска бота
async def main() -> None:

    config = load_config('.env')
    bot: Bot = Bot(config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())