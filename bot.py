import telebot
from telebot import types

# Вставь сюда свой токен от @BotFather
token = 'YOUR_TOKEN_HERE'

bot = telebot.TeleBot(token)

# Хранилище для текущего выражения
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('7', '8', '9', '/')
    markup.row('4', '5', '6', '*')
    markup.row('1', '2', '3', '-')
    markup.row('0', '.', '=', '+')
    markup.row('C', 'DEL')
    
    bot.send_message(message.chat.id, 'Привет! Я калькулятор-бот. Нажимай кнопки или пиши выражение.', reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def calculator(message):
    text = message.text
    chat_id = message.chat.id
    
    if text == 'C':
        user_data[chat_id] = ''
        bot.send_message(chat_id, 'Очищено!')
        return
    
    if text == 'DEL':
        if chat_id in user_data:
            user_data[chat_id] = user_data[chat_id][:-1]
        bot.send_message(chat_id, 'Удалено последний символ')
        return
    
    if text == '=':
        if chat_id in user_data and user_data[chat_id]:
            try:
                result = eval(user_data[chat_id])
                bot.send_message(chat_id, f'Результат: {result}')
                user_data[chat_id] = str(result)
            except:
                bot.send_message(chat_id, 'Ошибка в выражении!')
                user_data[chat_id] = ''
        return
    
    # Добавляем символ
    if chat_id not in user_data:
        user_data[chat_id] = ''
    user_data[chat_id] += text
    bot.send_message(chat_id, f'Текущее выражение: {user_data[chat_id]}')

print('Бот запущен...')
bot.infinity_polling()