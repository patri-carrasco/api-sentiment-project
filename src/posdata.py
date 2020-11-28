from config.configuration import db,collection

def insert_phrase(chat,character,phrase):
  # chequear los datos aquí

  dict_insert = {'chat':f'{chat}',
      "character": f'{character}',
      "phrase" :f'{phrase}'
      }
  collection.insert_one(dict_insert)

