from telegram.ext import ApplicationBuilder
import asyncio


async def send_initial_greeting(bot, chat_id):
    message1 = "Новая задача создана"
    message2 = "Задача обновлена"
    message3 = "Задача удалена"
    await bot.send_message(chat_id=chat_id, text=message3)


async def main():
    app = ApplicationBuilder().token("6732230608:AAGzub32sm9WyrQ9naEprjcBLTx8ZxTeB3w").build()  # токен бота, обновлять

    chat_id = "1380883194"
    await send_initial_greeting(app.bot, chat_id)


if __name__ == "__main__":
    asyncio.run(main())
