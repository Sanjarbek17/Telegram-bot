from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
x=None
def start(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    button=telegram.replykeyboardmarkup.ReplyKeyboardMarkup([
    ['/lotin','/krill']
    ],resize_keyboard=True)
    bot.sendMessage(chat_id,'Please choose one of these',reply_markup=button)
def lotink(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    global x
    x=True
    bot.sendMessage(chat_id,'Now send me text')
def krilll(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    global x
    x=False
    bot.sendMessage(chat_id,'Now send me text')
def lotin(update,context):
    bot=context.bot
    chat_id=update.message.chat.id
    txt=update.message.text
    if x==True:
        if txt[0]=='E' or txt[0]=='e':
            txt=txt.replace('E','Э')
            txt=txt.replace('e','э')
        txt=txt.replace('O\'','Ў')
        txt=txt.replace('o\'','ў')
        txt=txt.replace('v','в')
        txt=txt.replace('Ya','Я')
        txt=txt.replace('ya','я')
        txt=txt.replace('Ye','Е')
        txt=txt.replace('ye','е')
        txt=txt.replace('Yo','Ё')
        txt=txt.replace('yo','ё')
        txt=txt.replace('Yu','Ю')
        txt=txt.replace('yu','ю')
        txt=txt.replace('Ch','Ч')
        txt=txt.replace('ch','ч')
        txt=txt.replace('Sh','Ш')
        txt=txt.replace('sh','ш')
        txt=txt.replace('G\'','Ғ')
        txt=txt.replace('g\'','ғ')
        txt=txt.replace('a','а')
        txt=txt.replace('B','Б')
        txt=txt.replace('b','б')
        txt=txt.replace('V','В')
        txt=txt.replace('v','в')
        txt=txt.replace('G','Г')
        txt=txt.replace('g','г')
        txt=txt.replace('D','Д')
        txt=txt.replace('d','д')
        txt=txt.replace('J','Ж')
        txt=txt.replace('j','ж')
        txt=txt.replace('Z','З')
        txt=txt.replace('z','з')
        txt=txt.replace('I','И')
        txt=txt.replace('i','и')
        txt=txt.replace('Y','Й')
        txt=txt.replace('y','й')
        txt=txt.replace('K','К')
        txt=txt.replace('k','к')
        txt=txt.replace('L','Л')
        txt=txt.replace('l','л')
        txt=txt.replace('M','М')
        txt=txt.replace('m','м')
        txt=txt.replace('N','Н')
        txt=txt.replace('n','н')
        txt=txt.replace('O','О')
        txt=txt.replace('o','о')
        txt=txt.replace('P','П')
        txt=txt.replace('p','п')
        txt=txt.replace('R','Р')
        txt=txt.replace('r','р')
        txt=txt.replace('S','С')
        txt=txt.replace('s','с')
        txt=txt.replace('T','Т')
        txt=txt.replace('t','т')
        txt=txt.replace('U','У')
        txt=txt.replace('u','у')
        txt=txt.replace('F','Ф')
        txt=txt.replace('f','ф')
        txt=txt.replace('X','Х')
        txt=txt.replace('x','х')
        txt=txt.replace('\'','ъ')
        txt=txt.replace(' E',' Э')
        txt=txt.replace(' e',' э')
        txt=txt.replace('Q','Қ')
        txt=txt.replace('q','қ')
        txt=txt.replace('H','Ҳ')
        txt=txt.replace('h','ҳ')
        bot.send_message(chat_id,txt)
    if x==False:
        txt=txt.replace('в','v')
        txt=txt.replace('Я','Ya')
        txt=txt.replace('я','ya')
        txt=txt.replace('Е','E')
        txt=txt.replace('е','e')      
        txt=txt.replace(' Е','Ye')
        txt=txt.replace(' е','ye')
        txt=txt.replace('Ё','Yo')
        txt=txt.replace('ё','yo')
        txt=txt.replace('Ю','Yu')
        txt=txt.replace('ю','yu')
        txt=txt.replace('Ў','O\'')
        txt=txt.replace('ў','o\'')
        txt=txt.replace('Ч','Ch')
        txt=txt.replace('ч','ch')
        txt=txt.replace('Ш','Sh')
        txt=txt.replace('ш','sh')
        txt=txt.replace('Ғ','G\'')
        txt=txt.replace('ғ','g\'')
        txt=txt.replace('а','a')
        txt=txt.replace('Б','B')
        txt=txt.replace('б','b')
        txt=txt.replace('В','V')
        txt=txt.replace('в','v')
        txt=txt.replace('Г','G')
        txt=txt.replace('г','g')
        txt=txt.replace('Д','D')
        txt=txt.replace('д','d')
        txt=txt.replace('Ж','J')
        txt=txt.replace('ж','j')
        txt=txt.replace('З','Z')
        txt=txt.replace('з','z')
        txt=txt.replace('И','I')
        txt=txt.replace('и','i')
        txt=txt.replace('Й','Y')
        txt=txt.replace('й','y')
        txt=txt.replace('К','K')
        txt=txt.replace('к','k')
        txt=txt.replace('Л','L')
        txt=txt.replace('л','l')
        txt=txt.replace('М','M')
        txt=txt.replace('м','m')
        txt=txt.replace('Н','N')
        txt=txt.replace('н','n')
        txt=txt.replace('О','O')
        txt=txt.replace('о','o')
        txt=txt.replace('П','P')
        txt=txt.replace('п','p')
        txt=txt.replace('Р','R')
        txt=txt.replace('р','r')
        txt=txt.replace('С','S')
        txt=txt.replace('с','s')
        txt=txt.replace('Т','T')
        txt=txt.replace('т','t')
        txt=txt.replace('У','U')
        txt=txt.replace('у','u')
        txt=txt.replace('Ф','F')
        txt=txt.replace('ф','f')
        txt=txt.replace('Х','X')
        txt=txt.replace('х','x')
        txt=txt.replace('ъ','\'')
        txt=txt.replace('Э','E')
        txt=txt.replace('э','e')
        txt=txt.replace('Қ','Q')
        txt=txt.replace('қ','q')
        txt=txt.replace('Ҳ','H')
        txt=txt.replace('ҳ','h')
        bot.send_message(chat_id,txt)
updater=Updater(token='1395602363:AAHFmnjEMWTF9BJajHu2Pm8rdRSKgGM4dCo')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('lotin',lotink))
updater.dispatcher.add_handler(CommandHandler('krill',krilll))
updater.dispatcher.add_handler(MessageHandler(Filters.text,lotin))
updater.start_polling()
updater.idle()