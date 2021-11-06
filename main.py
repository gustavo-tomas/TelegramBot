import telegram.ext
from decouple import config
from commands import *

TOKEN = config("TOKEN")

def main():
  updater = telegram.ext.Updater(TOKEN, use_context=True)
  updater.dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
  updater.dispatcher.add_handler(telegram.ext.CommandHandler("help", help))
  updater.dispatcher.add_handler(telegram.ext.CommandHandler("poke", poke))
  updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

  updater.start_polling()
  updater.idle()
  return

if __name__ == "__main__":
  print("TelegramBot is ready!")
  main()