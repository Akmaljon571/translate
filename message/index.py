from aiogram import types

from keyboard.inline import inline_setting
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
    text = 'Assalomu Alaykum  translate botga hush kelibsiz!😇 \nTranslate qilinuvchi sozni yuboring'
    translate_text = language_api(text=text, id=user_id, default='uz')
    await message.answer(text=translate_text,
                         reply_markup=home_keyboard)


@dp.message_handler(text='Sozlash ⚙️')
async def setting(message: types.Message):
    user_id = message.from_user.id
    one = get_one(id=user_id)
    print(one)
    await message.answer(text=f'Hi', reply_markup=inline_setting())


@dp.message_handler()
async def translate(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    translate_text = language_api(text=text, id=user_id)
    await message.answer(translate_text)
