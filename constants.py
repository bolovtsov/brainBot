from typing import Any

program_SQL = f'SQL/Oracle это 10 недель:\n' \
              f'1 - Связи в базах данных\n' \
              f'2 - Создание таблиц\n' \
              f'3 - DML и индексы\n' \
              f'4 - Запросы к нескольким таблицам\n' \
              f'5 - Условия для агрегатных функций\n' \
              f'6 - Промышленный запрос\n' \
              f'7 - Транзакции, представления\n' \
              f'8 - Операторы, циклы\n' \
              f'9 - Курсоры, хранимые процедуры\n' \
              f'10 - Триггеры, исключения'

modules_Python_AI = f'Анализ данных на Python это 7 модулей:\n' \
                    f'1 - Введение в Python\n' \
                    f'2 - Библиотеки Python\n' \
                    f'3 - ООП и паттерны \n' \
                    f'4 - Математика для Анализа данных \n' \
                    f'5 - Машинное обучение\n' \
                    f'6 - Нейронные сети\n' \
                    f'7 - Кейсы в портфолио '

program_Excel = f'Базовый Excel это 6 недель:\n' \
                f'1 - Структура документа Excel\n' \
                f'2 - Базовое форматирование и фильтры\n' \
                f'3 - Google таблицы и автозаполнение \n' \
                f'4 - Ссылки и основные функции\n' \
                f'5 - Продвинутые функции\n' \
                f'6 - ВПР, ГПР, индексы и практические задачи\n'

free_Python_base = 'https://youtu.be/znRUCEXVjfk'

free_case_first = 'https://youtu.be/DAr7mqX7hqI'

free_ML_first = 'https://youtu.be/WZPIB-v5QPg'

welcome_message = f'Изучите Python от А до Я, анализ данных и нейросети\n' \
                  f'Мы первый в СНГ проект, где вы получаете специальность за символическую плату.\n' \
                  f'А мы зарабатываем на вашем трудоустройстве\n'

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