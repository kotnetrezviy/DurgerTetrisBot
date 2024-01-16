#!venv/bin/python
import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

import constants

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=constants.BOT_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def start(message: types.Message):
    start_markup = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text = "Play", web_app=WebAppInfo(url="https://github.com"))]])
    await message.answer("Welcome to @DurgetTetrisBot", reply_markup=start_markup)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())