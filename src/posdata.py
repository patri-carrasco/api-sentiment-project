from config.configuration import db, col_chat, col_user, col_phrase  

def add_user(name):
  """
      Esta función inserta los un nuevo usario
       arg:
          name        
  """

  dict_insert = {
    "character": name
  }
  
  
  search = dict_insert["character"]
 
  find_character = list(col_user.find({f'{search}':{"$eq":f'{name}'}}))
  
  if len(find_character) == 0:
    col_user.insert_one(dict_insert)
  else:
    return "There is already a character with that name"
  

def add_chat(chat_name, participants):
  """
      Esta función inserta un nuevo chat 
       arg:
          chat_name, participants     
  """
  dict_insert = {
    "chat":chat_name, 
    "participants" : participants  
    }
  
  find_chat = list(col_chat.find({"chat":{"$eq":chat_name}}))
  
  if len(find_chat) == 0:
   
    col_chat.insert_one(dict_insert)
  else:
    print("There is already a chat with that name")
  
  


def insert_phrase(chat,character,phrase):
  """
      Esta función inserta frase 
       arg:
          chat
          character
          phrase        
  """
  #falta comprobar si el texto ya esta 
  dict_insert = {'chat':f'{chat}',
      "character": f'{character}',
      "phrase" :f'{phrase}'
      }
  col_phrase.insert_one(dict_insert)