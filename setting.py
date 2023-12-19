from aiogram import Bot, Dispatcher
from environs import Env

env = Env()
env.read_env()

bot = Bot(token=env('BOT_TOKEN'))
dp = Dispatcher(bot=bot)

