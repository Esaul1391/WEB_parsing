from aiogram import Bot, dispatcher, executor, types
import os

bot = Bot(token='')
bot = Bot(token=os.getenv("TOKEN"))

