from config.configuration import db, col_chat, col_user, col_phrase



def phrasecharacter(character):
  '''
      Esta función devuelve las frases que dice un personaje
      arg:
        character = personaje 
      return:
        phrases = frases del personaje
  '''
    query = {"character":f"{character}"}
    phrases = list(col_phrase.find(query,{"_id":0,"character":1,"chat":1, "phrase":1}))
    
    return phrases

def senti_phrasecharacter(character):
  """
      Esta función devuelve las frases de un personaje para analizar el sentimiento
      arg:
        character = personaje 
      return:
        phrases = frases del personaje
  """
    
    query = {"character":f"{character}"}
    phrases = list(col_phrase.find(query,{"_id":0, "phrase":1}))
    
    return phrases


def show_chat():
  """
      Esta función devuelve los chats que tenemos en la base de datos
      
      return:
        chats = chats de la db
  """
  chats = list(col_chat.find({},{"_id":0, "participants":0}))
    
  return chats


def show_participants():
  """
      Esta función devuelve los participantes que tenemos en la base de datos
      
      return:
        participants = participantes de la db
  """
  participantes = list(col_user.find({},{"_id":0}))
    
  return participantes