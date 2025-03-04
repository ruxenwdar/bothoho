import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7825180037:AAE6FgrWg_5e3DCUIXKK6xA3V89g-jRPaKM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    send_webapp_button(msg.chat.id)

def send_webapp_button(cid):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="Тест на дальтонизм", url="https://github.com/ruxenwdar/bothoho.git"))
    markup.add(InlineKeyboardButton(text="Тест на IQ", url="https://github.com/ruxenwdar/bothoho.git"))
    markup.add(InlineKeyboardButton(text="Тест на психику", url="https://github.com/ruxenwdar/bothoho.git"))
    bot.send_message(cid, "Наши тесты:", reply_markup=markup)
bot.polling(none_stop=True)
