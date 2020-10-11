import telegram
from pprint import pprint
bot = telegram.Bot(token='1175464841:AAETPy_hg3fOfvTuLgrpvJd3Fzkde5r9PZQ')
lastid=-1
while True:
    update=bot.getUpdates()[-1]
    chat_id=update.message.chat.id
    text=update.message.text
    bid=update.update_id
    if lastid!=bid:
        print(text)
        bot.send_message(chat_id,text)
        lastid=bid