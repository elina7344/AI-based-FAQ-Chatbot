# pip install Flask>=1.0.0 chatterbot>=1.0.0 chatterbot-corpus>=1.2.0 SQLAlchemy>=1.2
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

 # Creating ChatBot Instance
chatbot = ChatBot('FAQBot')

conversation = [
    "What is your name?",
    "My name is FAQbot",
    "Are you a robot?",
    "Yes, I am a robot",
    "Who made you?",
    "Team bugs and bots made me",
    "How can you help me?"
    "I can give you all answers to your queries about AICTE",
    "Are you real?",
    "I am a chatbot which can answer FAQs on AICTE",
    "What do you do?",
    "I am there to assist you with your questions regarding AICTE organisation."
]


AICTE=[
    "What is AICTE?",
    "AICTE stands for all India council for technical education.",
    "When did AICTE act came into existence?",
    "It was found in 1987",
    "what are the objectives of AICTE?",
    "Quality promotion in Technical education.",
    "what are the mission of AICTE?",
    "Emphasis on developing high quality institutions, academic excellence and innovative research.",
    "What are some initiatives undertaken by AICTE?",
    "Jal shakti abhyan, One person one tree, Smart India Hackathon, SWAYAM (Any time anywhere learning)",
    "What is the motive of Startup contest by AICTE?",
    "To promote student driven innovation and startups",
    "What is Smart India Hackathon?",
    "It is an innovative product development competition.",
    "First chairman of AICTE was appointed on?",
    "2nd July, 1993.",
    "what is AICTE-Yuvak Scheme?",
    "It stands for YOUTH UNDERTAKING VISIT FOR ACQUIRING KNOWLEDGE.",
    "What is meant by AICTE LILAVATI AWARD?",
    "This award is given to AICTE approved institutions, who have undertaken remarkable intervention for the cause and made an impact.",
    "In which year was first smart India Hackathon held?",
    "First Smart India Hackathon was conducted in the year 2017.",
    "Why is Smart India Hackathon held every year?",
    "A unique initiative to identify new and disruptive digital solutions for solving the challenges faced by our country under the program of Smart India Hackathon 2017.",
    "What is PMSSS scheme J&K 2021-22?",
    "The Prime Ministers Special Scholarship Scheme(PMSSS) is provided to J&K Students to pursue undergraduate studies outside the State of Jammu and Kashmir.",
    "What is AICTE Environment policy?",
    "It includes environment conservation policy to create awareness about natural resources.",
    "Where is the head office of AICTE located?",
    "Head office of AICTE is located in New-Delhi.",
    "How to contact AICTE?",
    "011-26131576-78.",
    "Which year was the Right to education act passed?",
    "The Right to Education Bill came into existence in August 2009.",
    "What is the full form of AICTE KARMA?",
    "Kaushal Augmentation and Restructuring Mission of AICTE.",
    "Motive of AICTE KARMA policy?",
    "Kaushal Augmentation and Restructuring Mission of AICTE” (KARMA)  is for all AICTE approved institutions in the country to overcome the dual challenge of scarcity of skilled manpower in jobs and low skill level of those who are presently in jobs."

]


trainer = ListTrainer(chatbot)
trainer.train(conversation)
trainer.train(AICTE)


english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer_corpus = ChatterBotCorpusTrainer(english_bot)
trainer_corpus.train("chatterbot.corpus.english.greetings",
"chatterbot.corpus.english.conversations")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run()