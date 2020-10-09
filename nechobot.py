from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def hello(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    bot.sendMessage(chat_id,txt)
updater=Updater(token='1345758482:AAGWIdwbWrKaNQH5UcRUzBCrFyKvxsCivyA')
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))
updater.start_polling()
updater.idle()