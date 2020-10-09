from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
def hello(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    button=telegram.replykeyboardmarkup.ReplyKeyboardMarkup([
    ['7','8','9','/'],
    ['4','5','6','*']
    ])
    bot.sendMessage(chat_id,txt,reply_markup=button)
updater=Updater(token='1345758482:AAGWIdwbWrKaNQH5UcRUzBCrFyKvxsCivyA')
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))
updater.start_polling()
updater.idle()