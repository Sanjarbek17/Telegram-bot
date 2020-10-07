import telegram
from pprint import pprint
bot = telegram.Bot(token='1345758482:AAGWIdwbWrKaNQH5UcRUzBCrFyKvxsCivyA')
update=bot.getUpdates()[-1]
chat_id=update.message.chat.id
text=update.message.text
button=telegram.replykeyboardmarkup.ReplyKeyboardMarkup([
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','+'],
    ['0','.','=','-']
])
bot.send_message(chat_id,text,reply_markup=button)