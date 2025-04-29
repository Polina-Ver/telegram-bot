__all__ = [
    "router",
]

from aiogram.filters import Command
from aiogram import Router
from .keyboard import keyboards  # импорт из клавиатур
from .callbacks import callback_message  # импорт из коллбека

#Создание экземпляра объекта Router
router = Router()

@router.message(Command("help"))
async def process_help_command(message):
    '''Команда help'''
    await message.answer("Помощь пришла!", reply_markup=keyboards)

@router.message(Command(commands=["start", "status"]))
async def process_start_command(message):
    '''Команда status'''
    await message.reply(f"{message.from_user.id}, {message.from_user.username}")