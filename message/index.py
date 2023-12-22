from aiogram import types

from keyboard.inline import inline_setting, language_codes
from setting import dp
from keyboard.button import home_keyboard
from database.connect import get_one, create, update
from api.index import language_api
from setting import bot


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
    one_user = get_one(id=user_id)
    lang1 = ''
    lang2 = ''
    for a in language_codes:
        if a["code"] == one_user['lang1']:
            lang1 += a['key']
        elif a["code"] == one_user['lang2']:
            lang2 += a['key']
    text = f"Siz {lang1}dan {lang2}ga tarjima qilmoqchisiz..."
    translate_text = language_api(text=text, id=user_id, default='uz')
    await message.answer(text=translate_text, reply_markup=inline_setting())


@dp.callback_query_handler()
async def callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if callback.data != 'finish':
        data = callback.data.split(':')
        update(id=user_id, new_data={
            "user_id": user_id,
            "lang1": data[0],
            "lang2": data[1]
        })
        lang1 = ''
        lang2 = ''
        for a in language_codes:
            if a["code"] == data[0]:
                lang1 += a['key']
            elif a["code"] == data[1]:
                lang2 += a['key']
        text = f"Siz {lang1}dan {lang2}ga o`zgartirildi..."
        translate_text = language_api(text=text, id=user_id, default='uz')
        await bot.edit_message_text(chat_id=callback.message.chat.id,
                                    message_id=callback.message.message_id,
                                    text=translate_text,
                                    reply_markup=inline_setting())
    else:
        text = 'Tarjima qilinadigan so`zni yuboring...'
        translate_text = language_api(text=text, id=user_id, default='uz')
        await callback.message.answer(translate_text)
        await callback.message.delete()


@dp.message_handler()
async def translate(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    translate_text = language_api(text=text, id=user_id)
    await message.answer(translate_text)
