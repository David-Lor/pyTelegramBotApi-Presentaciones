"""
TelegramBot0

* Recibir comandos y responder
"""

import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def comm_start(message):
    chatid = message.chat.id
    userid = message.from_user.id
    bot.send_message(chatid, "Hola!")
    print("Recibí comando /start de chat {chat} y usuario {usuario}".format(
        chat=chatid,
        usuario=userid
    ))

@bot.message_handler(commands=["help","ayuda"])
def comm_help(message):
    bot.reply_to(message, "Ayúdame!!!")
    print("Recibí comando /help de chat {chat} y usuario {usuario}".format(
        chat=message.chat.id,
        usuario=message.from_user.id
    ))

bot.polling()
