from aiogram import executor

from setting import dp
import message.index

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
