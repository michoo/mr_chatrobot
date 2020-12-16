#!/usr/bin/env python

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

logging.basicConfig(level=logging.DEBUG)

chatbot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer',
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    './chatterbot_corpus/data/mr_robot/s01/',
    './chatterbot_corpus/data/mr_robot/s02/',
    './chatterbot_corpus/data/mr_robot/s03/',
    './chatterbot_corpus/data/mr_robot/s04/',
    # "./export.json",
    'chatterbot.corpus.english',

)
