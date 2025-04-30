import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router, set_my_commands  # Импортируем router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Подключаем роутер к диспетчеру
    dp.include_router(router)

    # Установка команд меню
    await set_my_commands(bot)

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())