#!/usr/bin/python
# -*- coding: utf-8-*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os, random, webbrowser

TOKEN = ''
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

confirmPhrases = ['Ok.', 'Alright.', 'Of course.', 'Count on me.', 'Done.', 'Okay', 'Leave it to me.',
'\'kay.', 'Understood.', 'That\'s okay.', 'I\'m doing it.', 'Yes.', 'Wait a second.', 'Oh, gimme a second.'
]
misunderstandingPhrases = ['Sorry.', 'Uh, what did you say?', 'Sorry, could you repeat that?', 'I didn\'t get the idea.',
        'What do you mean?', 'It doesn\'t makes sense.', "It doesn't sound right."]
listeningPhrases = ['Yes?', 'How can I help you?', "I'm listening you.", "I'm listening.", "Go on."]

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm Maid, what can I do for you?")

def echo(bot, update):
    if 'logoff' in update.message.text.lower():
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(confirmPhrases))
            os.system('shutdown -l')
    elif 'shutdown' in update.message.text.lower() or 'turn off' in update.message.text.lower():
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(confirmPhrases))
            os.system('shutdown /s')
    elif 'restart' in update.message.text.lower() or 'reboot' in update.message.text.lower():
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(confirmPhrases))
            os.system('shutdown /s')
    elif 'rock' in update.message.text.lower():
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(confirmPhrases))
            webbrowser.open_new_tab('https://www.youtube.com/watch?v=p80Yl9HQ5KI')
    elif 'jpop' in update.message.text.lower():
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(confirmPhrases))
            jpop = ['https://www.youtube.com/watch?v=bjHaQOisUCM&t=629s', 'https://www.youtube.com/watch?v=DYgqNZ349Ow&t=1098s', 'https://www.youtube.com/watch?v=T06xLIKdFVA&t=598s', 'https://www.youtube.com/watch?v=Ldg5WN1HEa8&t=2461s']
            webbrowser.open_new_tab(random.choice(jpop))
    elif 'rap' in update.message.text.lower():
            bot.send_message(chat_id=update.message.chat_id, text=random.choice(confirmPhrases))
            rap = ['https://www.youtube.com/watch?v=WVk6n-212Pw']
            webbrowser.open_new_tab(random.choice(rap))
    elif 'bye' in update.message.text.lower() or 'later' in update.message.text.lower():
            bot.send_message(chat_id=update.message.chat_id, text='~Bye! \ (•◡•) /')
    else:
            if 'maid' in update.message.text.lower():
                bot.send_message(chat_id=update.message.chat_id,  text=random.choice(listeningPhrases))
            else:
                bot.send_message(chat_id=update.message.chat_id,  text=random.choice(misunderstandingPhrases))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
