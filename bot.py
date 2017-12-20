# -*- coding: utf-8 -*-
import telepot, os

# Config vars
token = os.environ['TELEGRAM_TOKEN']

#material
gifBestemmia = 'https://raw.githubusercontent.com/prof18/RSS-Parser/master/Screen.png'
godImage = 'https://drive.google.com/open?id=1BdbMGEtJEF4g9v1DW3TlEzhPAhIyquOY'
siVocal = "https://drive.google.com/open?id=1UGuBto7q97m8qUWOiCH2bQYOoMrBlKgM"

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
    elif 'si' in msgText:
        bot.sendDocument(chat_id, gifBestemmia)


bot.message_loop({'chat': on_chat_message}, run_forever=True)
