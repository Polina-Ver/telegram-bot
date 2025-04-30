from aiogram.types import CallbackQuery
from aiogram import Router, F
router = Router()

@router.callback_query(F.data == 'life')
async def callback_message(call: CallbackQuery):
    await call.answer()
    await call.message.answer("продолжаешь жить своей унылой жизнью")

@router.callback_query(F.data == 'death')
async def callback_message(call: CallbackQuery):
    await call.answer()
    await call.message.answer("то же самое, только клубничная")