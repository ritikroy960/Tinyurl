import telebot
import pyshorteners

bot_token = "6828026036:AAGSiyrvQ1uQ88ODkAsXX9M-Q--3Zb2x4ak"
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, " Welcome to TinyUrl Bot! Send me a link and I'll Shorten it for you.")

@bot.message_handler(commands=['tinyurl'])
def send_tinyurl(message):
  url = message.text.split(' ', 1)[1]
  s = pyshorteners.Shortener()
  short_url = s.tinyurl.short(url)
  bot.reply_to(message, short_url)

bot.polling()
