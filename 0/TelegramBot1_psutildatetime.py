"""
TelegramBot1

* Recibir comando, responder y editar mensajes enviados.
* Formato de mensajes con Markdown y HTML.
* Añadir datos obtenidos de librerías psutil y datetime a nuestros mensajes.
"""

import telebot
import psutil
from datetime import datetime
from time import sleep

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


@bot.message_handler(commands=["cpu"])
def comm_cpu(message):
    
    def get_cpu():
        """
        Obtener porcentaje de uso de la CPU
        """
        return psutil.cpu_percent(interval=1) #Bloquea duante 1 segundo
    
    chatid = message.chat.id
    enviado = None #Aquí guardamos el mensaje que enviamos
    valores_cpu = list()

    for i in range(10): #Actualizar 10 veces

        cpu = get_cpu()
        valores_cpu.append(cpu)
        texto = "*Uso de CPU:* {}% _(#{})_".format(cpu, i+1)
        
        if not enviado: #Ejecución inicial
            enviado = bot.send_message(
                chat_id=chatid,
                text=texto,
                parse_mode="Markdown"
            )
        else: #Siguientes ejecuciones
            bot.edit_message_text(
                chat_id=chatid,
                message_id=enviado.message_id,
                text=texto,
                parse_mode="Markdown"
            )
    
    #Al terminar, mostrar la media de porcentajes
    media_cpu = sum(valores_cpu) / len(valores_cpu)
    media_cpu = round(media_cpu, 2)
    texto = "<b>Media de uso de CPU:</b> {}%".format(media_cpu)
    sleep(1)
    bot.edit_message_text(
        chat_id=chatid,
        message_id=enviado.message_id,
        text=texto,
        parse_mode="HTML"
    )


@bot.message_handler(commands=["cpudatetime"])
def comm_cpudatetime(message):
    
    def get_cpu():
        """
        Obtener porcentaje de uso de la CPU
        """
        return psutil.cpu_percent(interval=1) #Bloquea duante 1 segundo
    
    chatid = message.chat.id
    enviado = None #Aquí guardamos el mensaje que enviamos
    timestamp_inicial = None #Aquí guardamos cuándo se envió el primer mensaje
    timestamp_ultimo = None #Aquí guardamos cuándo se envió el último mensaje
    valores_cpu = list()

    for i in range(10): #Actualizar 10 veces

        cpu = get_cpu()
        timestamp = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        valores_cpu.append(cpu)
        texto = "*Uso de CPU:* {}% _({})_".format(cpu, timestamp)
        
        if not enviado: #Ejecución inicial
            enviado = bot.send_message(
                chat_id=chatid,
                text=texto,
                parse_mode="Markdown"
            )
            timestamp_inicial = timestamp
        else: #Siguientes ejecuciones
            bot.edit_message_text(
                chat_id=chatid,
                message_id=enviado.message_id,
                text=texto,
                parse_mode="Markdown"
            )
            timestamp_ultimo = timestamp
    
    #Al terminar, mostrar la media de porcentajes
    media_cpu = sum(valores_cpu) / len(valores_cpu)
    media_cpu = round(media_cpu, 2)
    texto = "<b>Media de uso de CPU:</b> {}%\n<i>Inicio: {}</i>\n<i>Fin: {}</i>".format(media_cpu, timestamp_inicial, timestamp_ultimo)
    sleep(1)
    bot.edit_message_text(
        chat_id=chatid,
        message_id=enviado.message_id,
        text=texto,
        parse_mode="HTML"
    )


bot.polling()
