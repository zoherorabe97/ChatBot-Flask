from app import app
import sqlite3
from chatterBot import Chatbot
if __name__ == '__main__':
    print(Chatbot.__version__)
    app.run()
