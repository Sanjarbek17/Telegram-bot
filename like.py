from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

token = os.environ['token']
lik=[]
dis=[]
def start(update, context):
    bot = context.bot
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'Send me photo')

def like(update, context):
    text = update.message.photo[0].file_id 
    like = InlineKeyboardButton(
        text=f'👍',
        callback_data='like'
    )
    dislike = InlineKeyboardButton(
        text='👎',
        callback_data='dislike'
    )
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[[like,dislike]])
    bot = context.bot
    chat_id = update.message.chat.id
    bot.sendPhoto(chat_id, text,reply_markup=reply_markup)
updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, like))

updater.start_polling()
updater.idle()
