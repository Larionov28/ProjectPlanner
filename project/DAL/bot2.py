from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

"""
from telegram import Bot
def send_telegram_message(message):
    bot = Bot(token='6732230608:AAEaMVcxt4QscAZ5Tb5ovmqhCOEeCGuUV2A')
    chat_id = '1380883194'
    bot.send_message(chat_id=chat_id, text=message)
"""


async def handle_messages(update: Update) -> None:
    text = update.message.text.lower()

    if "hello" in text:
        await update.message.reply_text("Здравствуйте, Артём Романович!")
    elif "howareyou" in text:
        await update.message.reply_text("Хорошо, у вас как?")
    elif "help" in text:
        await update.message.reply_text("Руководство использования:\n1)При вводе текста /hello, бот приветствует "
                                        "вас;\n2)При вводе текста /howareyou, бот отвечает 'Хорошо, "
                                        "как у вас?';\n3)При вводе текста /help, бот выводит руководство "
                                        "использования;\n4)При вводе любого другого текста, бот переотправляет "
                                        "сообщение;\n5)Также у бота есть встроенные команды.")
    else:
        # Если сообщение не соответствует заданным шаблонам, эхо-ответ
        await update.message.reply_text(update.message.text)


app = ApplicationBuilder().token("6732230608:AAEaMVcxt4QscAZ5Tb5ovmqhCOEeCGuUV2A").build()

# Добавляем обработчик сообщений с использованием filters
app.add_handler(MessageHandler(filters.Regex(r'.*'), callback=handle_messages))

app.run_polling()
