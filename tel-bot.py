#keys
from keys import api_key, api_secret, api_key_bot

from binance.client import Client
from binance.exceptions import BinanceAPIException
import telegram.ext
import re

client = Client(api_key, api_secret)

def start(update, context):
    update.message.reply_text('Este es el cryto bot')

def help(update, context):
    update.message.reply_text('''
    Comandos disponibles:
    /start -> Mensaje de bienvenida
    /price [par] -> Precio de un par (ej. BTCUSDT, SHIBBUSD)
    ''')

def price_handled(update, context):
    if re.match(r'price ', update.message.text, re.IGNORECASE):
        try:
            found = re.search(r'^price (.+)', update.message.text, re.IGNORECASE).group(1)
            update.message.reply_text(f'Precio: {found.split()[0]}')
        except AttributeError:
            update.message.reply_text('Comando erróneo :(')

def price(update, context):
    if len(context.args) > 0:
        ticker = context.args[0]
        ticker = ticker.upper()
        if ticker.isalpha():
            try:
                data = client.get_margin_price_index(symbol='BTCUSDT')
                pri = float(data['price'])
                update.message.reply_text(f'El precio de {ticker} es {pri:.2f}')
            except BinanceAPIException:
                update.message.reply_text('Error de par :(')


updater = telegram.ext.Updater(api_key_bot, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))
disp.add_handler(telegram.ext.CommandHandler('price', price))
#disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, price_handled))

updater.start_polling()
updater.idle()