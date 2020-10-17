from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, InlineQueryHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, KeyboardButton
# import os
# TOKEN = os.environ['TOKEN']
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
    button=InlineKeyboardButton('➕ Add to cart', callback_data='add')
    reply_markup=InlineKeyboardMarkup([
        [button]
    ])
    m=InputTextMessageContent(
        message_text='Chili Pizza(14")\n$22.99\n\nOriginal Signature crust, 100% whole milk mozzarella, Canadian-style bacon, applewood smoked bacon, sliced red onions, Dole® pineapple chunks, Kogi™ Serrano Chili sauce drizzle, and topped with fresh chopped cilantro.\n(https://c1.tchpt.com/admin/aux?b=c1~4066c4e45b62c35f92d362574ab3a0c91&a=c1~576&f=KogiSerranoChili_1024x768__2019-07-30_17-33-45.jpg)',
    )
    result2=InlineQueryResultArticle(
        title='Chili Pizza (14)',
        input_message_content=m,
        thumb_url='https://c1.tchpt.com/admin/aux?b=c1~4066c4e45b62c35f92d362574ab3a0c91&a=c1~576&f=KogiSerranoChili_1024x768__2019-07-30_17-33-45.jpg',
        description='$22.99',
        reply_markup=reply_markup,
        thumb_width=1,
        hide_url=True,
        id=1
    )
    result1=[result2]
    update.inline_query.answer(result1)
lst=[]
def add(update, context):
    query=update.callback_query
    data = query.data
    lst.append(data)
    query.answer('✅Added to cart')
    print(lst)
def cart(update, context):
    l=len(lst)
    bot=context.bot
    chat_id=update.message.chat.id
    button=InlineKeyboardButton(text='❌ Clear', callback_data='clear')
    button1=InlineKeyboardButton(text='✅ Place order', callback_data='place')
    reply_markup=InlineKeyboardMarkup([
        [button, button1]
    ])
    bot.sendMessage(chat_id,f'🛒 Cart\n\nChili Pizza (14") - $22.99x{l}=${22.99*l}\n\n💵 Total:${22.99*l}', reply_markup=reply_markup)
def clear(update, context):
    del lst[:]
    query=update.callback_query
    query.answer('Working')
    query.edit_message_text('✅ Cart cleared')
def place(update, context):
    bot=update.callback_query.bot
    chat_id=update.callback_query.message.chat.id
    button=KeyboardButton('Location', request_location=True)
    reply_markup=ReplyKeyboardMarkup([
        [button],
        ['❌ Cancel.']
    ], resize_keyboard=True)
    bot.sendMessage(chat_id,' 📍 Please send the address to which you want your order to be delivered.', reply_markup=reply_markup)
def location(update, context):
    bot=context.bot
    l=len(lst)
    chat_id=update.message.chat.id
    button=InlineKeyboardButton(text='❌ Clear', callback_data='clear')
    button1=InlineKeyboardButton(text='✅ Place order', callback_data='place')
    reply_markup=InlineKeyboardMarkup([
        [button, button1]
    ])
    bot.sendMessage(chat_id, '👍 Done! Now you can place orders.')
    bot.sendMessage(chat_id,f'🛒 Cart\n\nChili Pizza (14") - $22.99x{l}=${22.99*l}\n\n💵 Total:${22.99*l}', reply_markup=reply_markup)
updater=Updater(token='1175464841:AAEZ4Omez8DqnmmUCt_h2eTdUnAv3nBMDPs')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🎛 Administration'),Administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('❌ Cancel'), Administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('❌ Cancel.'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Location'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🚪 Exit'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🤑 Bonus rate'), Bonus))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Delete product'), Dproduct))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Remove category'), Rcategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('➕ Add category'), Acategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 New product'), Acategory))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👋 Welcome text'), Welcome))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏬 Catalog'), catalog))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'), cart))
updater.dispatcher.add_handler(MessageHandler(Filters.location, location))
updater.dispatcher.add_handler(CallbackQueryHandler(add, pattern='add'))
updater.dispatcher.add_handler(CallbackQueryHandler(place, pattern='place'))
updater.dispatcher.add_handler(CallbackQueryHandler(clear, pattern='clear'))
updater.dispatcher.add_handler(InlineQueryHandler(callback=inlinequery))
updater.start_polling()
updater.idle()
