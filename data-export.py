#!/usr/bin/env python

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer',
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(chatbot)


trainer.export_for_training('./export.yml')