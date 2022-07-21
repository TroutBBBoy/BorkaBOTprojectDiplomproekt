from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = settings.KEY

def start(update: Update, context: CallbackContext):
    mes="Привет, я BorkaBot,я немного туповат и ничего не умею, кроме как повторять за тобой"
    context.bot.send_message(chat_id=update.effective_chat.id, text=mes)

def talk_to_me(update: Update, context: CallbackContext):
    if update.message.text == "Привет":
        user_text = "И тебе Привет, {}".format(update.message.chat.first_name)
        logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                     update.message.chat.id, update.message.text)
    elif update.message.text == "Как дела?":
        user_text = "Спасибо за вопрос {}, у меня все хорошо, но хотелось бы немного поумнеть!!!".format(update.message.chat.first_name)
        logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                     update.message.chat.id, update.message.text)
    else:
        user_text= "Кажется ты написал: <{}>, чтобы это могло значить?!".format(update.message.text)
        logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                 update.message.chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=user_text)

def main():
    mybot = Updater(TOKEN)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()