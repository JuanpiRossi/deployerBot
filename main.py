from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram import InputTextMessageContent, ParseMode
import os
import tokenConfig

TOKEN = tokenConfig.BOT_TOKEN

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

allowed_users = ["528527409"]

def echo(bot,update,args):
    if str(update.message.from_user.id) in allowed_users:
        if args[0] == "metegol":
            os.system("sh /var/sources/deployer/deployMetegolBot")
            bot.send_message(chat_id=update.message.chat_id,text="deployeado!")
        else:
            bot.send_message(chat_id=update.message.chat_id,text="No se encontro la tarea de deploy: " + str(args[0]))
    else:
        bot.send_message(chat_id=update.message.chat_id,text="Falta autenticacion")

test_handler = CommandHandler('deploy',echo, pass_args=True)

dispatcher.add_handler(test_handler)

updater.start_polling()
updater.idle()
