from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, InlineQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
import os
TOKEN = os.environ['TOKEN']
def start(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt='Hello! 👋\nThis is a demo version of the Telegram Store bot. You can test out\n catalog function and checkout process. If you have questions, you\n can contact developer via Fiverr (https://www.fiverr.com/wrenaker), or directly here: @wren_aker'
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
def catalog(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    text=update.message.text
    button=InlineKeyboardButton('🍕Pizza', switch_inline_query_current_chat='pizza')
    reply_markup=InlineKeyboardMarkup([
        [button]
    ])
    bot.sendMessage(chat_id, text, reply_markup=reply_markup)
def inlinequery(update, context):
    msg=InputTextMessageContent(
        message_text='Chili Pizza(14")\n$22.99\n\nOriginal Signature crust, 100% whole milk mozzarella, Canadian-style bacon, applewood smoked bacon, sliced red onions, Dole® pineapple chunks, Kogi™ Serrano Chili sauce drizzle, and topped with fresh chopped cilantro.\n(https://c1.tchpt.com/admin/aux?b=c1~4066c4e45b62c35f92d362574ab3a0c91&a=c1~576&f=KogiSerranoChili_1024x768__2019-07-30_17-33-45.jpg)',
    )
    result=InlineQueryResultArticle(
        title='Chili Pizza (14)',
        input_message_content=msg,
        thumb_url='https://c1.tchpt.com/admin/aux?b=c1~4066c4e45b62c35f92d362574ab3a0c91&a=c1~576&f=KogiSerranoChili_1024x768__2019-07-30_17-33-45.jpg',
        description='$22.99',
        hide_url=True,
        id=1
    )
    result1=[result]
    update.inline_query.answer(result1)
    
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
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏬 Catalog'), catalog))
updater.dispatcher.add_handler(InlineQueryHandler(callback=inlinequery))
updater.start_polling()
updater.idle()
