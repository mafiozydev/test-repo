import telebot
import random

from telebot import types

# Вставь сюда свой токен от @BotFather
token = 'YOUR_TOKEN_HERE'

bot = telebot.TeleBot(token)

jokes = [
    "Почему программисты путают Хеллоуин и Рождество? Потому что Oct 31 == Dec 25!",
    "Как называется страх длинных слов? Гиппопотомонстросесквипедалиофобия.",
    "— Почему Python такой популярный? — Потому что он не Java!",
    "Debugging: being the detective in a crime movie where you are also the murderer.",
    "Есть только 10 типов людей: те, кто понимает двоичную систему, и те, кто нет."
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add('Шутку!', 'Ещё шутку', 'Мем', '/help')
    bot.send_message(message.chat.id, 'Привет! Я мемный Echo-бот 😂\nНажимай кнопки или просто пиши мне.', reply_markup=markup)

@bot.message_handler(commands=['joke', 'help'])
def send_joke(message):
    joke = random.choice(jokes)
    bot.send_message(message.chat.id, joke)

@bot.message_handler(func=lambda m: True)
def echo(message):
    text = message.text.lower()
    
    if 'шутк' in text or 'joke' in text:
        joke = random.choice(jokes)
        bot.send_message(message.chat.id, joke)
    elif text == 'мем':
        bot.send_message(message.chat.id, 'Мемов пока нет, но вот шутка: ' + random.choice(jokes))
    else:
        bot.send_message(message.chat.id, f'Ты написал: {message.text}\nЯ эхо-бот, но иногда шучу 😎')

print('Мемный бот запущен...')
bot.infinity_polling()