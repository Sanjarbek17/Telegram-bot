from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
import os
import requests
from pprint import pprint
import json
token1 = os.environ['token1']
def start(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    print(chat_id)
    text='Give me your location'
    button2=KeyboardButton('location', request_location=True)
    button=ReplyKeyboardMarkup([
        [button2]
    ], resize_keyboard=True)
    bot.send_message(chat_id, text, reply_markup=button)
def location(update, context):
    bot=context.bot
    chat_id=update.message.chat.id
    # location=update.message.location
    longitude=update.message.location.longitude
    latitude=update.message.location.latitude
    payload={
        'lat':latitude,
        'lon':longitude,
        'units':'metric',
        'appid':'0cbfc3d170d767140f3bcad4835235fb'
    }
    response=requests.get('https://api.openweathermap.org/data/2.5/onecall', params=payload)
    data=response.json()
    current=data['current']
    clouds=current['clouds']
    humidity=current['humidity']
    weather_decs=current['weather'][0]['description']
    icon=current['weather'][0]['icon']
    text=f'clouds: {clouds}\nWeather description: {weather_decs}\nhumidity: {humidity}\nIcon: {icon}'
    bot.send_message(chat_id, text)
updater= Updater(token=str(token1))
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.location,location))
updater.start_polling()
updater.idle() 