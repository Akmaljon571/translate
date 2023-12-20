from aiogram import types

from setting import dp
from keyboard.button import home_keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Assalomu Alaykum  translate botga hush kelibsiz!😇 \n translate qilinuvchi sozni yuboring', reply_markup=home_keyboard)
