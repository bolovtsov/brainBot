import telebot
import os
import constants

bot = telebot.TeleBot(os.environ.get('TOKEN'))


@bot.message_handler(content_types=['text'])
def any_messages(message):
    keyboard_main = telebot.types.InlineKeyboardMarkup(row_width=2)
    about_company_button = telebot.types.InlineKeyboardButton(text='О Brainskills', callback_data="about")
    courses_button = telebot.types.InlineKeyboardButton(text='курсы', callback_data="courses")
    free_button = telebot.types.InlineKeyboardButton(text='материалы', callback_data="free")
    registration_button = telebot.types.InlineKeyboardButton(text='мероприятия', callback_data="registration")
    keyboard_main.add(about_company_button)
    keyboard_main.add(courses_button, free_button)
    keyboard_main.add(registration_button)
    bot.send_message(message.chat.id, text="Что интересно?", reply_markup=keyboard_main)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        keyboard_main = telebot.types.InlineKeyboardMarkup(row_width=2)
        about_company_button = telebot.types.InlineKeyboardButton(text='О Brainskills', callback_data="about")
        courses_button = telebot.types.InlineKeyboardButton(text='курсы', callback_data="courses")
        free_button = telebot.types.InlineKeyboardButton(text='материалы', callback_data="free")
        registration_button = telebot.types.InlineKeyboardButton(text='мероприятия', callback_data="registration")
        keyboard_main.add(about_company_button, courses_button, free_button, registration_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="то интересно?",
                              reply_markup=keyboard_main)
    if call.data == "courses":
        keyboard_courses = telebot.types.InlineKeyboardMarkup()
        python_button = telebot.types.InlineKeyboardButton(text='Анализ данных на Python', callback_data="python")
        sql_button = telebot.types.InlineKeyboardButton(text='SQL/Oracle', callback_data="sql")
        excel_button = telebot.types.InlineKeyboardButton(text='Базовый Excel', callback_data="excel")
        back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data="mainmenu")
        keyboard_courses.add(python_button, sql_button, excel_button, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Курсы",
                              reply_markup=keyboard_courses)
    if call.data == "free":
        keyboard_free = telebot.types.InlineKeyboardMarkup()
        base_python_button = telebot.types.InlineKeyboardButton(text='материалы по Python', callback_data='free_base_py')
        case_button = telebot.types.InlineKeyboardButton(text='кейс', callback_data='free_case')
        ml_button = telebot.types.InlineKeyboardButton(text='материалы по ML', callback_data='free_ML')
        back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data="mainmenu")
        keyboard_free.add(base_python_button, case_button, ml_button, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Материалы",
                              reply_markup=keyboard_free)
    if call.data == "about":
        keyboard_about = telebot.types.InlineKeyboardMarkup()
        back_button = telebot.types.InlineKeyboardButton(text='Назад', callback_data="mainmenu")
        keyboard_about.add(back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=constants.welcome_message,  reply_markup=keyboard_about)


bot.polling(none_stop=True)

"""@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока')
    bot.send_message(message.chat.id, 'Приветствуем вас в сообществе Brainskills!!!', reply_markup=keyboard)"""
