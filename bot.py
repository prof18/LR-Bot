# -*- coding: utf-8 -*-
import telepot
import os

# Config vars
token = os.environ['TELEGRAM_TOKEN']

# material
gifBestemmia = os.environ['GIF_BEST']
godImage = os.environ['GOD_IMAGE']

bot = telepot.Bot(token)


def on_chat_message(msg):

    # CHAT META

    # chat id
    chat_id = msg['chat']['id']
    # message text lower cased for matching purpouse
    msgText = msg['text']
    msgText = msgText.lower()
    # Name
    firstName = msg['from']['first_name']
    # Surname
    lastName = msg['from']['last_name']

    if 'ciao luca rossi' in msgText:
        bot.sendMessage(chat_id, ("Tara no!"))
    elif 'come stai' in msgText:
        bot.sendMessage(chat_id, ("Oggi cominci male!"))
    elif 'sei pronto' in msgText:
        bot.sendMessage(chat_id, ("Che ansia"))
    elif 'lr' in msgText:
        bot.sendDocument(chat_id, gifBestemmia)
    elif 'dio' in msgText:
        bot.sendPhoto(chat_id, godImage)


bot.message_loop({'chat': on_chat_message}, run_forever=True)
