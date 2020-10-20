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
    button=InlineKeyboardButton('Nikai', switch_inline_query_current_chat='nikai')
    button2=InlineKeyboardButton('Emerald', switch_inline_query_current_chat='emerald')
    button3=InlineKeyboardButton('Marwa', switch_inline_query_current_chat='marwa')
    reply_markup=InlineKeyboardMarkup([
        [button,button2],
        [button3]
    ])
    bot.sendMessage(chat_id, text, reply_markup=reply_markup)
lid=[]
def photo(update, context):
    sid=update.message.photo[0].file_id
    lid.append(sid)
    print(lid)
def nikai(update, context):
    txt2='Odul'
    odul='https://raw.githubusercontent.com/Sanjar1218/Telegram-bot/master/odul.jpg'
    fresh='https://raw.githubusercontent.com/Sanjar1218/Telegram-bot/master/fresh.jpg'
    pechka='https://raw.githubusercontent.com/Sanjar1218/Telegram-bot/master/pechka.jpg'
    pechka1='https://raw.githubusercontent.com/Sanjar1218/Telegram-bot/master/pechka1.jpg'
    utok='https://raw.githubusercontent.com/Sanjar1218/Telegram-bot/master/utok.jpg'
    m=InputTextMessageContent(
        message_text=f'[Odul]({odul})s {txt2}',
        parse_mode='MarkdownV2'
    )
    m2=InputTextMessageContent(
        message_text=f'[Fresh]({fresh})s {txt2}',
        parse_mode='MarkdownV2'
    )
    m3=InputTextMessageContent(
        message_text=f'[Pechka]({pechka})s {txt2}',
        parse_mode='MarkdownV2'
    )
    m4=InputTextMessageContent(
        message_text=f'[pechka1]({pechka1})s {txt2}',
        parse_mode='MarkdownV2'
    )
    m5=InputTextMessageContent(
        message_text=f'[Utok]({utok})s {txt2}',
        parse_mode='MarkdownV2'
    )
    result5=InlineQueryResultArticle(
        title='Utok',
        input_message_content=m5,
        thumb_url=utok,
        description='$22.99',
        hide_url=True,
        id=5
    )
    result4=InlineQueryResultArticle(
        title='Pechka1',
        input_message_content=m4,
        thumb_url=pechka1,
        description='$22.99',
        hide_url=True,
        id=4
    )
    result3=InlineQueryResultArticle(
        title='Pechka',
        input_message_content=m3,
        thumb_url=pechka,
        description='$22.99',
        hide_url=True,
        id=3
    )
    result1=InlineQueryResultArticle(
        title='Odul',
        input_message_content=m2,
        thumb_url=odul,
        description='$22.99',
        hide_url=True,
        id=1
    )
    result2=InlineQueryResultArticle(
        title='Fresh',
        input_message_content=m,
        thumb_url=fresh,
        description='$22.99',
        hide_url=True,
        id=2
    )
    result=[result1,result2,result3,result4,result5]
    update.inline_query.answer(result)
def emerald(update, context):
    emerald='https://images-aka.kay.com/kay/gemstone/2020/hero_updates/k_aug20_gemstone_emerald.jpg'
    txt2='soda'
    m1=InputTextMessageContent(
        message_text=f'[Emerald]({emerald}) {txt2}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='Emerald',
        input_message_content=m1,
        thumb_url=emerald,
        description='$0.0',
        hide_url=True,
        id=2
    )
    result=[result1]
    update.inline_query.answer(result)
def marwa(update, context):    
    marwa='https://images.muslimnames.com/marwa_muslim_girls_names_meaning_islamic_girls_names.png'
    txt2='soda'
    m2=InputTextMessageContent(
        message_text=f'[Marwa]({marwa}) {txt2}',
        parse_mode='MarkdownV2'
    )
    result1=InlineQueryResultArticle(
        title='Marwa',
        input_message_content=m2,
        thumb_url=marwa,
        description='$0.0',
        hide_url=True,
        id=3
    )
    result=[result1]
    update.inline_query.answer(result)
lst=[]
lst1=[]
def add(update, context):
    query=update.callback_query
    id=query.inline_message_id
    print(query)
    data = query.data
    lst.append(data)
    query.edit_message_text(id)
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
def order(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    button=InlineKeyboardButton('❌ Cancel.', callback_data='cancel')
    reply_markup=InlineKeyboardMarkup([
        [button]
    ])
    bot.sendMessage(chat_id, '✍️ Order #1602922406 (SETTING)\n🛒 Order list:\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Amount to pay: $22.99\n\n💬 Comment to the order: None\n📍 Delivery address: bulungur', reply_markup=reply_markup)
def cancel(update, context):
    query=update.callback_query
    query.edit_message_text('❌ Order cancelled')
def userinfo(update, context):
    bot=context.bot
    first=update.message.chat.first_name
    chat_id=update.message.chat.id
    button=InlineKeyboardButton('🗺Addresses', callback_data='addresses')
    button2=InlineKeyboardButton('➕ Add address', callback_data='address')
    reply_markup=InlineKeyboardMarkup([
        [button, button2]
    ])
    bot.sendMessage(chat_id, f'👤 {first}\n🤝 Invited friends: 0\n💸 Bonus balance: $0.0\nℹ️ You can get 5.0% on your bonus balance from the amount of each order of your invited friends.\n🔗 Your referral link: https://t.me/demosellerbot?start=555351863', reply_markup=reply_markup)

updater=Updater(token='1396169156:AAEtmTZvh-L_3FGTG_u7E5Fn2HtOyqkj0dI')
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
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 Orders'), order))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👤 Userinfo'), userinfo))
updater.dispatcher.add_handler(MessageHandler(Filters.location, location))
updater.dispatcher.add_handler(CallbackQueryHandler(add, pattern='add'))
updater.dispatcher.add_handler(CallbackQueryHandler(place, pattern='place'))
updater.dispatcher.add_handler(CallbackQueryHandler(clear, pattern='clear'))
updater.dispatcher.add_handler(CallbackQueryHandler(cancel, pattern='cancel'))
updater.dispatcher.add_handler(InlineQueryHandler(nikai, pattern='nikai'))
updater.dispatcher.add_handler(InlineQueryHandler(emerald, pattern='emerald'))
updater.dispatcher.add_handler(InlineQueryHandler(marwa, pattern='marwa'))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo))
updater.start_polling()
updater.idle()