import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv("URL")

if not (DBURL):
  raise ValueError("Tiene que especificar una URL")


client = MongoClient(DBURL)
db = client.get_database()


col_chat = db["chats"]
col_user = db["user"]
col_phrase = db['phrase']


