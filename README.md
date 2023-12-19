# Telegram Tarjima Boti

Bu Telegram boti, foydalanuvchilarga kiritilgan matnlarni boshqa tillarga tarjima qilish imkoniyatini taqdim etadi.

## O'rnatish

1. Repositorni yuklab olish:
    ```bash
    git clone https://github.com/sizning-forkingiz/telegram-tarjima-bot.git
    cd telegram-tarjima-bot
    ```

2. Talab etilgan kutubxonalarini o'rnating:
    ```bash
    pip install -r requirements.txt
    ```

## Sozlash

1. [BotFather](https://core.telegram.org/bots#botfather) orqali yangi bot yarating va API kalitini oling.
2. `.env` faylini yaratib, unga API kalitingizni qo'shing:
    ```env
    API_TOKEN=Botning_API_kaliti
    ```

## Ishga Tushirish

Ishga tushirish uchun quyidagi komandani ishga tushuring:
```bash
python bot.py
