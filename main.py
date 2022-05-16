import telebot
from telebot import types

bot = telebot.TeleBot('5319575996:AAELLX1sFEa0YeIsnVFiy_obGUhcqOgyP2Q')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# Отслеживаем ввод текста и реагируем на определенный текст!!!
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'И тебе, привет', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('wtf.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю!', parse_mode='html')

# Отслеживаем отправку боту файла (на примере фотографии)
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')

# Отслеживаем ввод команды боту (на примере гиперссылки)
@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://www.linkedin.com/in/%D0%B0%D0%BB%D0%B5%D0%'
                                                                   'BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80-%D0%BB%D1%83%D0%B'
                                                                   'A%D0%BE%D0%BC%D1%81%D0%BA%D0%B8%D0%B9-90393523a/'))
    bot.send_message(message.chat.id, 'Залетай!', reply_markup=markup)


# Добавляем кнопки в чат при вызове команды "help"
@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Вебсайт')
    start = types.KeyboardButton('Старт')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Залетай!', reply_markup=markup)



bot.polling(none_stop=True)
