from aiogram import types

from setting import dp

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Hi')
