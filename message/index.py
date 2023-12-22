from aiogram import types

from setting import dp
from keyboard.button import home_keyboard
from database.connect import get_one, create
from api.index import language_api


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if not get_one(id=user_id):
        create(data={
            "user_id": user_id,
            "lang1": "en",
            "lang2": "uz"
        })
    await message.answer('Assalomu Alaykum  translate botga hush kelibsiz!😇 \nTranslate qilinuvchi sozni yuboring',
                         reply_markup=home_keyboard)

@dp.message_handler()
async def translate(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    translate_text = language_api(text=text, id=user_id)
    await message.answer(translate_text)
