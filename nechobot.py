from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
def start(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    text=update.message.text
    button=telegram.replymarkup.ReplyMarkup([
        ['salom']
    ])
    bot.send_message(chat_id, text, reply_markup=button)
updater= Updater(token='1159902341:AAG37H4f31qdH5OB2-2LEMNMrTAJDo2OeQ4')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.start_polling()
updater.idle() 