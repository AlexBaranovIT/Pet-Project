from telebot import TeleBot, types
import os

TOKEN = 'YOUR TELEGRAM BOT TOKEN'
bot = TeleBot(TOKEN)

#Function that reacts on command start
@bot.message_handler(commands=['start']):
def start(message):
    welcome_message = 'Hello, ' + message.from_user.first_name + message.from_user.last_name
    bot.send_message(message.chat.id, welcome_message)


#Bot watching updates
bot.polling(none_stop=True)
