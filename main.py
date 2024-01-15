#!venv/bin/python
import asyncio
import logging

from aiogram import Bot, Dispatcher,types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters.command import Command

import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(config.BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open url', web_app=WebAppInfo(url='https://kotnetrezviy.github.io/DurgerTetrisBot')))
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())