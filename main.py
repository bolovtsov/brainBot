import telebot
import os
import constants

bot = telebot.TeleBot(os.environ.get('TOKEN'))

@bot.message_handler(content_types=['text'])
def any_messages(message):
    key_board_main = telebot.types.InlineKeyboardMarkup(row_width=4)
    about_company_button = telebot.types.InlineKeyboardButton(text='О Brainskills', callback_data="about")
    courses_button = telebot.types.InlineKeyboardButton(text='курсы', callback_data="courses")
    free_button = telebot.types.InlineKeyboardButton(text='материалы', callback_data="free")
    registration_button = telebot.types.InlineKeyboardButton(text='мероприятия', callback_data="registration")
    key_board_main.add(about_company_button, courses_button, free_button, registration_button)
    bot.send_message(message.chat.id, text="Что интересно?", reply_markup=key_board_main)


"""@bot.message_handler(commands=['help'])
def help_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='SQL/Oracle', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Анализ данных на Python', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Базовый Excel', callback_data=3))
    bot.send_message(message.chat.id, text="Какая программа вас интересует?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Not bad!')
    answer = ''
    if call.data == '1':
        answer = constants.program_SQL
    elif call.data == '2':
        answer = constants.modules_Python_AI
    elif call.data == '3':
        answer = constants.program_Excel
    elif call.data == '10':
        answer = constants.free_Python_base
    elif call.data == '11':
        answer = constants.free_case_first
    elif call.data == '12':
        answer = constants.free_ML_first
    elif call.data == '20':
        get_ex_callback(call)
        answer = ''
    elif call.data == '21':
        #help_message()
        answer = constants.free_ML_first
    elif call.data == '22':
        #setting_message()
        answer = constants.free_ML_first
    elif call.data == '23':
        #setting_message()
        answer = constants.free_ML_first
    bot.send_message(call.message.chat.id, answer)

def get_ex_callback(call):
    bot.answer_callback_query(call.id)
    help_message(call.data)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='О Brainskills', callback_data=20))
    markup.add(telebot.types.InlineKeyboardButton(text='программы курсов Brainskills', callback_data=21))
    markup.add(telebot.types.InlineKeyboardButton(text='бесплатные материалы по Python, кейс и ML', callback_data=22))
    markup.add(telebot.types.InlineKeyboardButton(text='регистрация на бесплатные материалы', callback_data=23))
    bot.send_message(message.chat.id, text="Выберете одно из действий:", reply_markup=markup)

    bot.reply_to(message, f'Приветствуем вас в сообществе Brainskills, {message.from_user.first_name}!\n'
                          f'{constants.welcome_message}'
                          )


@bot.message_handler(commands=['setting'])
def setting_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Бесплатные материалы по Python', callback_data=10))
    markup.add(telebot.types.InlineKeyboardButton(text='Бесплатные кейс', callback_data=11))
    markup.add(telebot.types.InlineKeyboardButton(text='Бесплатные материалы по Python', callback_data=12))
    bot.send_message(message.chat.id, text="Что по плечу?", reply_markup=markup)"""


bot.polling(none_stop=True)

"""@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока')
    bot.send_message(message.chat.id, 'Приветствуем вас в сообществе Brainskills!!!', reply_markup=keyboard)"""