from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    text='sen'
    bot.send_message(chat_id, text)
def sticker(update, context):
    f=open('file_id.txt','a')
    bot=context.bot
    chat_id=update.message.chat.id
    file_id=update.message.sticker.file_id
    f.write(str(file_id))
    bot.send_message(chat_id, file_id)
def hi(update, context):
    f=open('file_id.txt','a')
    bot=context.bot
    chat_id=update.message.chat.id
    file_id=update.message.sticker.file_id
    f.write(str(file_id))
    bot.send_message(chat_id, file_id)
updater= Updater(token='1159902341:AAG37H4f31qdH5OB2-2LEMNMrTAJDo2OeQ4')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.sticker,sticker))
updater.start_polling()
updater.idle() 