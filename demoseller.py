from telegram.ext import CommandHandler, MessageHandler,Updater,Filters
from telegram import ReplyKeyboardMarkup
import os
TOKEN = os.environ['TOKEN']
def start(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    button=ReplyKeyboardMarkup([
        ['🏬 Catalog','📦 Orders'],
        ["👤 Userinfo","🛒 Cart"],
        ['🎛 Administration']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Administration(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    button=ReplyKeyboardMarkup([
        ['👥 Users','🏷  Orders'],
        ['👋 Welcome text','🤑 Bonus rate'],
        ['➕ Add category','🗑 Remove category'],
        ['📦 New product','🗑 Delete product'],
        ['🚪 Exit']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Welcome(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='Write what you want it doesn\'t matter'
    button=ReplyKeyboardMarkup([
        ['❌ Cancel']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Bonus(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='Write what you want it doesn\'t matter'
    button=ReplyKeyboardMarkup([
        ['❌ Cancel']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,txt,reply_markup=button)
def Dproduct(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
def Rcategory(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
def Acategory(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
def Nproduct(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='⚡️ Not available in fake version.'
    bot.sendMessage(chat_id,txt)
updater=Updater(token=str(TOKEN))
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🎛 Administration'),Administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('❌ Cancel'), Administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🚪 Exit'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🤑 Bonus rate'), Bonus))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Delete product'), Dproduct))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Remove category'), Rcategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('➕ Add category'), Acategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 New product'), Acategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👋 Welcome text'), Welcome))
updater.start_polling()
updater.idle()
