import sys
import time

sys.dont_write_bytecode = True
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django

django.setup()

from db.models import *

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(force_reply=True, input_field_placeholder='salom'),
    )


def help(update, context):
    while True:
        sekund = 0
        minut = 0
        soat = 0
        a = int(input("Son kiriting: "))

        for x in range(1, a + 1):
            time.sleep(1)
            sekund += 1
            if sekund < 60:
                print(f'{x} - sekund')
            elif sekund > 60:
                minut = sekund // 60
                print(f'{minut} - minut, {x % 60} - sekund')

def echo(update, context):
    update.message.reply_text(update.message.text)


updater = Updater("5207306118:AAGwuNaq2lpiHNCSmx-wTlNp2meRzMn4sBo")

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))

dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
