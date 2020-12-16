#!/usr/bin/env python

import random

from chatterbot import ChatBot
from chatterbot.conversation import Statement
from termcolor import colored
from lib.leet import leet_converter, emoji
from lib.tts import tts
from lib.banner import after_start

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)


chatbot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # some logic adapters but I can't make it work on my computer
    # logic_adapters=[
    #     'chatterbot.logic.MathematicalEvaluation',
    #     'chatterbot.logic.TimeLogicAdapter',
    #     'chatterbot.logic.BestMatch'
    # ],
    trainer='chatterbot.trainers.ListTrainer',
    database_uri='sqlite:///database.db'
)


def get_feedback():
    print('D0 y0u W4n7 70 134rn? (yes,y or no,n,enter)')
    text = input()

    if 'yes' in text.lower():
        return (True, text)
    elif 'y' in text.lower():
        return (True, text)
    else:
        return (False, text)

# Banner
after_start()

# first user input
user_input = input()

# The following loop will execute each time the user enters input
# I know the user_input order is not appropriate and seems complicated but 
# I tried to implement feedback so that's why...
while True:
    try:
        if user_input[:1] == '/':
            # Do something else like a cmd, it's for a future project
            user_input = input()
        else:
            bot_response = chatbot.get_response(user_input)
            original_message = bot_response.text
            message = leet_converter(bot_response.text)
            if bot_response.confidence > 0.2:
                text = colored(message, 'green')
                print(text)

                # Text To Speech function
                tts(original_message)

            else:
                text = colored(message, 'red')
                print(text)

                # Text To Speech function
                tts(original_message)

                # If you want to give some feedback to your bot
                # (correction, text) = get_feedback()
                # if correction is True:
                #     print('L34rn me s0mething...')
                #     correct_response = Statement(text=input())
                #     chatbot.learn_response(correct_response, user_input)
                #     original_message = correct_response
                #     text = colored(original_message, 'green')
                #     print(text)
                #     tts(original_message)
            user_input = input()


    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
