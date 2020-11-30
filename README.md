# Creando una API de Friends
<div style="text-align:center"><img src="https://blog.ticketmaster.es/wp-content/uploads/2018/08/que-fue-actores-friends-1.jpg" height=300 /></div> 

# **Introducción**

En este proyecto vamos analizar sentimientos de un grupo de chat.

Para ello hemos creado una API con los mensajes que se han enviado en los personajes de la  serie Friends.



# ¿Cómo funciona?

 - **/new/user**
  Con este endpoint insertaremos nuevos personajes a la base de datos.

 ```
  character = {
    "character : "Rachel",
  }
  ```


  - **/new/phrase**
  Con este endpoint insertaremos frases a la base de datos.

  ```
  phrase = {
    "chats": "girls_friends",
    "character : "Rachel",
    "phrase" : "Hello"
  }
  ``` 

  - **/new/chat**
  Con este endpoint insertaremos nuevos personajes a la base de datos.

  ```
  chat = {
    "chats": "girls_friends",
    "participants :['Rachel', 'Monica', 'Phoebe']
  }
  ```
 - **/sentiment/character**
 Con este endpoint analizaremos las frases los sentimientos de las frases de un personaje