from config.configuration import db, col_chat, col_user, col_phrase



def phrasecharacter(character):
    query = {"character":f"{character}"}
    phrases = list(col_phrase.find(query,{"_id":0,"character":1,"chat":1, "phrase":1}))
    
    return phrases

def senti_phrasecharacter(character):
    
    query = {"character":f"{character}"}
    phrases = list(col_phrase.find(query,{"_id":0, "phrase":1}))
    
    return phrases


def show_chat():
  
  chats = list(col_chat.find({},{"_id":0, "participants":0}))
    
  return chats


def show_participants():
  participantes = list(col_user.find({},{"_id":0}))
    
  return participantes