import telebot
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import constans

bot = telebot.TeleBot(constans.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Приветствуем вас в сообществе Brainskills!!!, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

@bot.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=bot.greet_kb)

bot.polling(none_stop=True)