import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

load_dotenv()
token = os.getenv('TOKEN')


async def start(update, context):
    await update.message.reply_text("""Bienvenue sur le bot, Pour commencer a spot:
    - /spot""")


if __name__ == '__main__':
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start))

    app.run_polling(poll_interval=5)
