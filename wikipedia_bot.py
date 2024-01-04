import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.full_name}")



@dp.message_handler()
async def echo(message: types.Message):
    matn = message.text
    await message.reply(wikipedia.summary(matn))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)