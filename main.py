import telebot
import constans

bot = telebot.TeleBot(constans.token)

"""@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока')
    bot.send_message(message.chat.id, 'Приветствуем вас в сообществе Brainskills!!!', reply_markup=keyboard)"""


@bot.message_handler(commands=['help'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Введение в Python', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Анализ данных на Python', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='SQL/Oracle', callback_data=3))
    bot.send_message(message.chat.id, text="Какая программа вас интересует?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == '1':
        answer = f'Программа состоит из 10 недель:\n' \
                 f'1 - Связи в базах данных\n' \
                 f'2 - Создание таблиц\n' \
                 f'3 - DML и индексы \n' \
                 f'4 - Запросы к нескольким таблицам\n ' \
                 f'5 - Условия для агрегатных функций\n ' \
                 f'6 - Промышленный запрос\n ' \
                 f'7 - Транзакции, представления ' \
                 f'8 - Операторы, циклы ' \
                 f'9 - Курсоры, хранимые процедуры ' \
                 f'10 - Триггеры, исключения '
    elif call.data == '2':
        answer = f'Программа состоит из 7 модулей:\n' \
                 f'1 - Введение в Python\n2 - Библиотеки Python\n3 - ООП и ' \
                 f'паттерны \n4 - Математика для Анализа данных \n ' \
                 f'5 - Машинное обучение\n6 - Нейронные сети\n 7 - ' \
                 f'7 - Кейсы в портфолио '
    elif call.data == '3':
        answer = f'Программа состоит из 6 недель:\n' \
                 f'1 - Структура документа Excel\n' \
                 f'2 - Базовое форматирование и фильтры\n' \
                 f'3 - Google таблицы и автозаполнение \n' \
                 f'4 - Ссылки и основные функции\n ' \
                 f'5 - Продвинутые функции\n ' \
                 f'6 - ВПР, ГПР, индексы и практические задачи\n '
    bot.send_message(call.message.chat.id, answer)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Приветствуем вас в сообществе Brainskills, {message.from_user.first_name}!\n'
                          f'Здесь вы можете:\n'
                          f'/help узнать как работает подписка Brainskills\n'
                          f'/setting получать бесплатные материалы по Python, ML/DL, AI\n'
                          f'/action регистрироваться на бесплатные мероприятия')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
