from importlib import resources
from flask import Flask
import chatterbot
from chatterbot import ChatBot
from flask_cors.decorator import  cross_origin
from flask_cors.extension import  CORS

from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
CORS(app , resources = {r"/api/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
bot = ChatBot('zoher')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')


from app import view

