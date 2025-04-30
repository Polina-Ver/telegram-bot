from aiogram.filters import Command
from aiogram import Router, types
from .keyboard import keyboards

router = Router()  # Создаем один роутер для всех обработчиков

@router.message(Command("help"))
async def process_help_command(message: types.Message):
    await message.answer("Помощь пришла!", reply_markup=keyboards)

@router.message(Command(commands=["start", "status"]))
async def process_start_command(message: types.Message):
    await message.reply(f"{message.from_user.id}, {message.from_user.username}")