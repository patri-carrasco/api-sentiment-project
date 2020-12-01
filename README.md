# Creando una API de Friends
<div style="text-align:center"><img src="https://blog.ticketmaster.es/wp-content/uploads/2018/08/que-fue-actores-friends-1.jpg" height=300 /></div> 



# **Introducción**

En este proyecto vamos analizar sentimientos de un grupo de chat.

Para ello hemos creado una API con los mensajes que se han enviado en los personajes de la  serie Friends.
 
 # **Descripción**

 En este proyecto hemos usado FLASK para poder generar la API donde analizaremos si los mensajes entre los miembros de los grupos de chats son positivos o negativos.

 # **Estructura del repo**

 Hemos estructurado el proyecto en varios archivos y carpetas para que sea más fácil su entendimiento.
  - Config, carpeta que  usamos para la configuración básica del proyecto.
  - data carpeta donde va los archivos datos.
  - src carpeta que guarda todos los archivos de funciones que usamos en este proyecto:

    getdata.py :archivo que tiene las funciones de GET de la api.

    postdata.py: archivo que tiene las funciones POST de la api.

    sentiment.py: archivo que tiene las funciones que analiza los sentimientos de los mensajes.
  - api.py:Este es el archivo principal de la API.

# **Enlaces usados**

- https://www.kaggle.com/blessondensil294/friends-tv-series-screenplay-script?select=S01E02+The+Sonogram+At+The+End.txt



# **Libreías usadas**
- sys

- requests

- json

- load_dotenv

 - os

 - nltk

- flask, Flask, request

- markdown extensions fenced_code

