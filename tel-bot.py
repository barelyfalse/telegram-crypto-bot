#keys
from keys import api_key, api_secret, api_key_bot

from binance.client import Client
from binance.exceptions import BinanceAPIException
import telegram.ext

def start(update, context):
    update.message.reply_text('Welcome to crypto bot')

def help(update, context):
    update.message.reply_text('''
    Comandos disponibles:
    /start -> Welcome message
    /price [coin] -> Price
    ''')

def price(update, context):
    update.message.reply_text(f'Mensaje: {update.message.text}')

updater = telegram.ext.Updater(api_key_bot, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()