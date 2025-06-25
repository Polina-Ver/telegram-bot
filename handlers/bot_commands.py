from aiogram import Bot
from aiogram.types import BotCommand


async def set_my_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запуск бота"),
        BotCommand(command="/help", description="Вывод справочной информации"),
        BotCommand(command="/status", description="Вывод статуса пользователя"),
        BotCommand(command="/getres", description="Посмотреть задачи студентов"),
        BotCommand(command="/checked", description="Ваши задачи проверены преподавателем")

    ]
    await bot.set_my_commands(commands)