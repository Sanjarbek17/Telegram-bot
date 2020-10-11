from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
# import telegram
def start(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    inline=InlineKeyboardButton('salom', callback_data='nothing')
    button=InlineKeyboardMarkup([
        ['salom',inline]
    ])
    bot.sendMessage(chat_id,txt, reply_markup=button)
updater=Updater(token='1159902341:AAG37H4f31qdH5OB2-2LEMNMrTAJDo2OeQ4')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.start_polling()
updater.idle()
