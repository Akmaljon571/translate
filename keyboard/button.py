from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [
    [KeyboardButton(text='Sozlash ⚙️')]
]

home_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
