# Spaceship-Game

Spaceship es un juego creado a partir de la programacion enfocada en objetos, fue creada con ayuda de pygame y con una serie de clases en la que se iban inplementando avances.

## Estructura del proyecto

Esta devidida en en 3 partes clave, "assets", "components" y "utils", en estas se han ido implementando dsitintas funcionalidades principales para el propio funcionamiento del juego, tanto sus actualizaciones, los reseteos, enemigos, etc.

## Game

El objetivo del juego es intentar sobrevivir el mayor tiempo posible mientras eliminas naves enemigas, esquivas obstaculos y vas obteniendo una puntuacion, en cada oportunidad de juego podras ir mejorando tu puntuacion y tienes una pequeña ayuda que vendria siendo un escudo que te facilita evitar los disparos enemigos, pero aun te tienes que cuidar de los obstaculos ya que el escudo no te protejera de impactar con ellos.

## Player

El jugador controlara una nave que en un inicio aparecera en la parte inferior central de la pantalla, apartir de ahi podras ir moviendote hacia cualquier lado utilizando las teclas (A, W, S, D) y podras disparar usando la barra espaciadora, tu movimiento sera limitado hasta la mitad de la pantalla.

# Enemigos

## Naves 

Existen dos enemigos de tipo nave, una es de color rojo con nehro denominada "Ship" su comportamiento es basico solo ira de un lado al otro de la pantalla disparando hacia abajo hasta salir de la pantalla detras del jugador al destruirla te dara 1 punto.

Mientras que la segunda siendo una nave de color Blanco denominada "Spider_ship" sigue las bases de su compañera pero con una velocidad aumentada en su movimiento lateral y en su disparo pero mas lenta en su movimiento descendente y a su vez tiene un intervalo mas corto para cambiar de direccion, al destruila te otorgara 3 puntos.

## Obstaculos

Existen igualmente 2 tipos de obstaculos, el primero siendo unos Meteoritos que caeran aleatoriamente de la parte superior de la pantalla a uan velocidad bastante considerable en linea recta, estos no podras destruirlos y tendras que esquivarlos ya que al chocar con el jugador ambos moriran.

Mientras que los otros son misiles que quedaron varados en el espacio, estos se moveran de la parte inferior izquierda en linea recta hacia la derecha evitando que te quedes mucho tiempo estatico en una posicion inicial, estos igualmente no son destruibles por lo que tendras que evitarlos de la manera mas rapida posible.

Inteta evitar los obstaculos a toda costa si no quieres perder tu puntuacion.

# Balas 

En el juego solo existen 2 tipos de balas las primeras vendrian siendo pequeñas balas tipo laser que son las que dispararan los 2 tipos de enemigos.

Mientras que las otras son balas comunes que disparara el jugador para derrotar a esos enemigos.

# Power Up

En el juego solo existe un power up que te ayudara a evitar nada mas los disparos enemigos, durara 10 segundos cada vez que lo atrapes y es de gran ayuda ya que solo tendras que enfocarte en esquivar los obstaculos.

# Menu 

En el menu principal del juego tendras 3 opciones las cuales podras alternar entre cada una usando las flechas del teclado, entre estas opciones podras Salir del juego, ver la maxima puntuacion obtenida e iniar el juego podras acceder a cada una de ellas utilizando la tecla enter de tu teclado.

# Game Over

Cada vez que pierdas en el juego regresaras al menu principal del juego con la diferencia de que la maxima puntuacion se ira actualizando y en la parte inferior del menu podras observar la puntuacion que conseguiste en la partida y la cantidad de intentos.