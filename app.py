from flask import Flask
import telebot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pyshorteners

app = Flask(__name__)

app.route('/')
def index():
    return 'Hello from Flask!'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0.', port=81)

token = '6897542653:AAGT0HgIgo428jKMgJggov0xi_8EejwMfw8'

bot = telebot.TeleBot(token)

@bot.message_handler(['start'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Hii👋 {name}\n Welcome to TinyUrl Shortner Bot! Send me a link and I'll Shorten it for you.", reply_markup=InlineKeyboardMarkup(start_button))

@bot.message_handler(['tinyurl'])
def send_tinyurl(message):
    try:
        url = message.text.split(' ', 1)[1]
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        bot.reply_to(message, 'YOUR LINK GOT SHORTENED\n ' + short_url)

    except:
        bot.reply_to(message, "i'm sorry, i can't capable to short bulk links")

@bot.message_handler()
def dend(message):
    bot.reply_to(message, "Please send Link in This Format\n /tinyurl http://example.com ")

start_button = [[
  InlineKeyboardButton("JOIN UPDATE CHANNEL", url="https://t.me/devx_coder"),
  InlineKeyboardButton("DEVELOPER", url="https://replit.com/@priyanshu999")
]]

bot.polling()
