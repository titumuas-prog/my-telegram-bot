import os
from flask import Flask
from threading import Thread
import telebot

TOKEN = "9269235276:AAHuqEqYexqSRqdTrmRey63nBFWIu7kVlvM"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "أهلا! البوت شغال 24 ساعة ✅")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"وصلتني: {m.text}")

@app.route('/')
def home():
    return "Bot OK"

def run_bot():
    bot.infinity_polling()

Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
