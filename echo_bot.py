import telegram
from pprint import pprint
bot = telegram.Bot(token='1345758482:AAGWIdwbWrKaNQH5UcRUzBCrFyKvxsCivyA')
while True:
    update=bot.getUpdates()[-1]
    chat_id=update.message.chat.id
    text=update.message.text
    bot.send_message(chat_id,text)
