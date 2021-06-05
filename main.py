import telebot
from telebot import types

import constans

bot = telebot.TeleBot(constans.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Приветствуем вас в сообществе Brainskills!, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

@bot.message_handler(commands = ['help'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт', url='https://brainskills.live')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)

bot.polling(none_stop=True)