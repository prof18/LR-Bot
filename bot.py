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
    chat_id = msg['chat']['id']  # prelevo id del mittente
    msgText = msg['text']  # prelevo testo del messaggio
    # username = msg['chat']['username'] #prelevo username del mittente

    # Log su shell
    print('Command Received ' + msgText)

    firstName = msg['from']['first_name']
    lastName = msg['from']['last_name']
    msgText = msgText.lower()

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
