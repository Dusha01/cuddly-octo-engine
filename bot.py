import logging
from aiogram import Bot, Dispatcher, executor, types

import cfg

bot = Bot(cfg.TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! 😊 \nЯ простой Telegram-бот, который повторяет ваши сообщения. 👉👈")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
