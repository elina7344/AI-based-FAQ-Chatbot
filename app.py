# pip install Flask>=1.0.0 chatterbot>=1.0.0 chatterbot-corpus>=1.2.0 SQLAlchemy>=1.2
from flask import Flask, render_template, request
from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# # Creating ChatBot Instance
# chatbot = ChatBot('FAQBot')
#
# conversation = [
#     "What is your name?",
#     "My name is Chatterbot",
#     "How old are you?",
#     "Im as old as sci-fi films"
# ]
#
#
# trainer = ListTrainer(chatbot)
# trainer.train(conversation)


english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer_corpus = ChatterBotCorpusTrainer(english_bot)
trainer_corpus.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run()
