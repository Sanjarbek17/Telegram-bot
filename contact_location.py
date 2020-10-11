from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
import os
token= os.environ['token']
def start(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    text='Give me your phone number or your location'
    button1=KeyboardButton('contact', request_contact=True)
    button2=KeyboardButton('location', request_location=True)
    button=ReplyKeyboardMarkup([
        [button1],
        [button2]
    ], resize_keyboard=True)
    bot.send_message(chat_id, text, reply_markup=button)
def contact(update, context):
    f=open('contact.txt', 'a')
    bot=context.bot
    chat_id=update.message.chat.id
    text='Telefon raqam uchun rahmat'
    contact=update.message.contact
    x=str(contact)+'\n'
    f.write(str(x))
    bot.send_message(chat_id, text)
def location(update, context):
    f=open('location.txt', 'a')
    bot=context.bot
    chat_id=update.message.chat.id
    location=update.message.location
    x=str(location)+'\n'
    f.write(str(x))
    text='Manzil uchun rahmat'
    location=update.message.location
    f.write(str(location))
    bot.send_message(chat_id, text)
updater= Updater(token=str(token))
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.contact,contact))
updater.dispatcher.add_handler(MessageHandler(Filters.location,location))
updater.start_polling()
updater.idle() 