from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_setting():
    language_codes = [{'key': '🇺🇿', 'code': 'uz'},
                      {'key': '🏴󠁧󠁢󠁥󠁮󠁧󠁿', 'code': 'en'},
                      {'key': '🇵🇹', 'code': 'pt'},
                      {'key': '🇷🇺', 'code': 'ru'},
                      {'key': '🇰🇷', 'code': 'ko'}]
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for i, a in enumerate(language_codes):
        if i != 0:
            buttons.append(InlineKeyboardButton(text=f"{language_codes[0]['key']} to {a['key']}",
                                                callback_data=f"{language_codes[0]['code']}:{a['code']}"))
            buttons.append(InlineKeyboardButton(text=f"{a['key']} to {language_codes[0]['key']}",
                                                callback_data=f"{a['code']}:{language_codes[0]['code']}"))
    keyboard.add(*buttons)
    return keyboard
