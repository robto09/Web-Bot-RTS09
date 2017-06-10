# Manual de Usuario Proyecto Web-Bot

El Web-Bot, es un bot programado en el lenguaje de programación python usando el micro-framework Flask,el cual podrá programarse mediante el envio de mensajes que le permitan al bot aplicar luego dichas operaciones mediante solicitudes previas.

Objetivo de este manual.

El objetivo primordial de éste manual es ayudar y guiar al usuario a utilizar el bot. Por lo tanto, se detallará una serie de pasos para ponerlo a funcionar en donde se indicará los comandos que deben ser escritos para su funcionamiento. Y comprender como utilizar el sistema.

Dirigido A:

Este manual está orientado a una parte de los Usuarios Finales involucrados en la etapa de Operación Bot, es decir para estudiantes del curso de servicios web que van a interactuar con el Bot.

Lo que se debe de conocer:

Los conocimientos mínimos que deben tener las personas que utilizarán el Bot y deberán utilizar este manual son:

Conocimientos básicos de Navegación en Web.
Conocimiento básico de Internet.
Conocimiento básico de Windows.
Conocimiento básico en programación.

Indice Funcionalidad

Para poder realizar consultas o interactuar con el Bot se deberá utilizar un cliente HTTP Rest como Postman, cURL o el de su preferencia.

1. Mostrar Estado (Muestra el Log de operaciones)

Para mostrar los estados, es decir el log de las actividades realizadas por los clientes que consulten al Bot se debe realizar una petición de tipo GET. Para ello debe introducir la siguiente url en la herramienta de su preferencia.

http://127.0.0.1/api/web-bot/mostrar/estados

2. Mostrar lista de conocimientos

Para mostrar la lista de conocimientos, es decir lo que sabe hacer el Bot,se debe realizar una petición de tipo GET. Para ello debe introducir la siguiente url en la herramienta de su preferencia.

http://127.0.0.1/api/web-bot/mostrar/memoria


3. Aprender (Agregar funcionalidad a la memoria de habilidades que tiene el WEB-BOT)

Para que el bot pueda aprenderlas habilidades se debe realizar una petición de tipo POST. En donde además de subirse el fichero con la habilidad que se requiere que aprenda también debe enviarse tres parámetros los cuales indican el nombre de la habilidad, el creador y el nombre de usuario. Por ejemplo  usando cURL para que el Bot aprenda la habilidad “saludo” se emplea el siguiente url.

curl -i -F 'file=@suma.py' http://127.0.0.1/5000/api/web-bot/aprender -F 'nombre=suma' -F 'creador=Robert' -F 'user=rts09'

Posteriormente para ejecutar la habilidad aprendida se usa el url propio de cada habilidad. Incluyendo además sus respectivos parametros.

curl -i -d 'op1=34&op2=8'  http://127.0.0.1:5000/api/web-bot/sumar


Al incluir la opción -d, estamos indicando al programa curl que envíe los datos mediante una petición POST. Además la opción -i nos añadirá también la cabecera devuelta por el servidor.

4. Desaprender (Eliminar funcionalidad de memoria de habilidades)

Para que el bot pueda desapender habilidades se debe realizar una petición de tipo DELETE. En donde se envian dos parámetros el userid y el nombre de la habilidad que se desea eliminar. Por ejemplo  usando cURL para que el Bot desaprenda la habilidad “saludo” se emplea el siguiente url.

http://127.0.0.1:5000/api/web-bot/mostrar/desaprender/<userid>/<nombre>

Ejemplo

http://127.0.0.1:5000/api/web-bot/mostrar/desaprender/<63055>/<saludo>





