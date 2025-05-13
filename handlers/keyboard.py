from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Inline-кнопка "Далее"
#Inline-кнопка "Слушатель"
#Inline-кнопка "Преподаватель"

button_continue = InlineKeyboardButton(text="Далее", callback_data="button_continue")
button_tutor = InlineKeyboardButton(text="Слушатель", callback_data="button_tutor")
button_student = InlineKeyboardButton(text="Преподаватель", callback_data="button_student")

#Inline-клавиатура "Продолжить"
#Inline-клавиатура "Выберите роль"
keyboard_continue = InlineKeyboardMarkup(inline_keyboard=[
        [button_continue, ]
    ])

keyboard_start = InlineKeyboardMarkup(inline_keyboard=[
        [button_student, button_tutor]
    ])




#button1 = InlineKeyboardButton(
   # text="СИНЯЯ ТАБЛЕТКА",
    #callback_data="life"
#)
#button2 = InlineKeyboardButton(
   # text="КРАСНАЯ ТАБЛЕТКА",
   # callback_data="death"
#)

#keyboards = InlineKeyboardMarkup(
  #  inline_keyboard=[
   #     [button1, button2]
   # ],
   # resize_keyboard=True,
   # one_time_keyboard=True
#)