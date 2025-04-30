import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router as router_handlers
from handlers import set_my_commands
from handlers.callbacks import router as router_callbacks

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    #Определение маршрутизации для диспетчера из handlers
    dp.include_routers(router_handlers, router_callbacks)

    # Установка команд меню
    await set_my_commands(bot)

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())