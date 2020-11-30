from config.configuration import db, col_chat, col_user, col_phrase

def getdata():

  #query = {"name": f'{name}'}
  #frases = list(collection.find(query,{"_id":0}))
  return "Hola"


def phrasecharacter(character):
    

    query = {"character":f"{character}"}
    phrases = list(col_phrase.find(query,{"_id":0,"character":1,"chat":1, "phrase":1}))
    
    return phrases