from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton(
    text="СИНЯЯ ТАБЛЕТКА",
    callback_data="life"
)
button2 = InlineKeyboardButton(
    text="КРАСНАЯ ТАБЛЕТКА",
    callback_data="death"
)

keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [button1, button2]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)