from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram import InputTextMessageContent, ParseMode
import os
import tokenConfig

TOKEN = tokenConfig.BOT_TOKEN

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def echo(bot,update):
    if str(update.message.from_user.id) == "528527409":
        os.system("sh /var/sources/deployer/deployMetegolBot")
        bot.send_message(chat_id=update.message.chat_id,text="deployeado!")
    else:
        bot.send_message(chat_id=update.message.chat_id,text="Falta autenticacion")

test_handler = CommandHandler('deploy',echo)

dispatcher.add_handler(test_handler)

updater.start_polling()
updater.idle()
