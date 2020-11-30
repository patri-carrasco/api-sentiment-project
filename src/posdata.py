from config.configuration import db, col_chat, col_user, col_phrase  

def add_user(name):
  
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
  dict_insert = {
    'chat':f'{chat_name}',
    'participants' : participants
  }
  col_chat.insert_one(dict_insert)




def insert_phrase(chat,character,phrase):
  # chequear los datos aquí

  dict_insert = {'chat':f'{chat}',
      "character": f'{character}',
      "phrase" :f'{phrase}'
      }
  col_phrase.insert_one(dict_insert)