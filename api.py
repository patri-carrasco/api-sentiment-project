from flask import Flask, request
from flask import request
import markdown.extensions.fenced_code

import  src.getdata as get
import src.posdata  as pos
import src.sentiment as sen
import json

#Start:  sudo systemctl start mongod
#status: sudo systemctl  status mongod


app = Flask(__name__)


@app.route("/")
def index():
  readme_file = open("index.md","r")
  md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
  return md_template_string



# functions post

@app.route("/new/user",methods=["POST"])
def new_user():
  character = request.form.get("character")
  pos.add_user(character)
  return "Ok, character entered correctly"


@app.route("/new/chat", methods = ["POST"])
def new_chat():
  
  chat = request.form.get("chat")
  participants = request.form.getlist("participants")
  print(f'Entra en new_chat participantes {participants},')
  pos.add_chat(chat,participants)

  return "Ok, character entered correctly"


@app.route("/new/phrase", methods = ["POST"])
def newphrase():
  chat = request.form.get("chat")
  character = request.form.get("character")
  phrase = request.form.get("phrase")
  pos.insert_phrase(chat,character,phrase)
  return "Ok,message entered correctly"

# functions get 
@app.route("/phrases/<character>")
def phrase_character(character):
    phrases = get.phrasecharacter(character)
    return json.dumps(phrases)

@app.route("/chats")
def show_chat():
    chats = get.show_chat()
    return json.dumps(chats)


@app.route("/participants")
def show_participants():
  participants = get.show_participants()
  return json.dumps(participants)


 # functions sentiment
@app.route("/sentiment/character/<character>")
def sentiment_character(character):
  print("ok")
  phrases = get.senti_phrasecharacter(character)
  sentiment = sen.sentiment(phrases,character)
  return json.dumps(sentiment)



app.run(debug = True)