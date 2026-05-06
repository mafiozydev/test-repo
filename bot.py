import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'YOUR_TOKEN_HERE'

jokes = [
    "Почему программисты путают Хеллоуин и Рождество? Потому что Oct 31 == Dec 25!",
    "Как называется страх длинных слов? Гиппопотомонстросесквиппедалиофобия.",
    "— Почему Python такой популярный? — Потому что он не заставляет тебя писать ; в конце каждой строки!"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Расскажи шутку 😂", callback_data='joke')],
        [InlineKeyboardButton("Кто я?", callback_data='about')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я мемный бот для теста GitHub pull'ов 🚀\n\nНажми кнопки или просто напиши мне что-нибудь.", 
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'joke':
        await query.edit_message_text(text=random.choice(jokes))
    elif query.data == 'about':
        await query.edit_message_text(text="Я простой тестовый бот. Создан для проверки скорости git pull с Grok.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'привет' in text or 'здарова' in text:
        await update.message.reply_text("Здарова, братело! 🔥")
    elif 'как дела' in text:
        await update.message.reply_text("Нормально, кодю с Grok'ом! А у тебя как?")
    else:
        await update.message.reply_text(f"Эхо: {update.message.text}")

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(jokes))

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
