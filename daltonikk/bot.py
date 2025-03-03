import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = "7825180037:AAE6FgrWg_5e3DCUIXKK6xA3V89g-jRPaKM"

test_url = "aibar.html"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Пройти тест", web_app=WebAppInfo(url=test_url))
    )
    await message.reply("Привет! Нажмите кнопку ниже, чтобы пройти тест на дальтонизм.", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
