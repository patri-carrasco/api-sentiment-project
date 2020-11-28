from flask import Flask, request
import markdown.extensions.fenced_code

import  src.getdata as get
import src.posdata  as pos
import json

#Start:  sudo systemctl start mongod
#status: sudo systemctl  status mongod


app = Flask(__name__)


@app.route("/")
def index():
  readme_file = open("README.md","r")
  md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
  return md_template_string



@app.route("/get_data")
def get_data():
  data = get.getdata()
  return data


@app.route("/newphrase", methods = ["POST"])
def newphrase():
  chat = request.form.get("chat")
  character = request.form.get("character")
  phrase = request.form.get("phrase")
  pos.insert_phrase(chat,character,phrase)
  return "Ok,message entered correctly"



app.run(debug = True)