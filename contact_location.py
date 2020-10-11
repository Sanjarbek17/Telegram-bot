from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
import os
token= os.environ['token']
print(token)
def start(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    print(chat_id)
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
    txt=str(contact.first_name)+':'+str(contact.phone_number)
    bot.send_message(555351863, txt)
def location(update, context):
    f=open('location.txt', 'a')
    bot=context.bot
    chat_id=update.message.chat.id
    location=update.message.location
    text='Manzil uchun rahmat'
    longitude=update.message.location.longitude
    latitude=update.message.location.latitude
    f.write(str(location))
    bot.send_message(chat_id, text)
    bot.send_location(555351863,latitude, longitude)
updater= Updater(token=str(token))
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.contact,contact))
updater.dispatcher.add_handler(MessageHandler(Filters.location,location))
updater.start_polling()
updater.idle() 