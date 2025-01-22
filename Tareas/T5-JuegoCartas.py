"""
Sofia Trezza
Seccion 2

Tarea 5
Genere 52 cartas
Tome los números del 1 al 13
Concaténelos con las diferentes pintas de cartas (treboles, diamantes, picas, corazones) 
para formar una lista de 52 cartas representadas como Strings ("1 de treboles", "1 de diamantes", etc.)
Barajee las cartas
Genere números al azar para elegir una carta de la lista
La carta en esa posición de la lista deberá ser movida a una nueva lista 
(debe asegurarse de no elegir la misma carta dos veces) que llamaremos el mazo barajado
Reparta las cartas, una a la vez
Pida entrada del usuario e imprima la siguiente carta de la lista cada vez que la pida
¡Batalla!
Si aparecen dos cartas seguidas del mismo valor (comenzando con el mismo número), 
y el usuario introduce "batalla", se le asignará un punto.
Si aparecen dos cartas del mismo valor y el usuario solicita la siguiente carta sin escribir "batalla", 
la computadora deberá imprimir "¡Batalla!" y asignarse a sí misma un punto
Fin
Al agotar todas las cartas del mazo barajado, se indicará cuántos puntos tiene el jugador humano, 
cuántos puntos tiene la computadora, y quién ganó
"""

import random
mazo=[]
#creamos las cartas en listas
valores=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
pintas=['treboles','diamantes','picas','corazones']

#creamos las combinaciones de las cartas
for valor in valores:
    for pinta in pintas:
        carta= str(valor)+ ' de ' +str(pinta)
        mazo.append(carta)
#barajamos
random.shuffle(mazo)
#definimos los contadores del juego
puntos_jugador=0
puntos_computadora=0
carta_anterior=None #necesitamos una variable para comparar y al principio esta carta no tiene nada
mazo_barajado=[]
#definimos el bucle del juego

#empezamos el juego
while mazo: #mientras que el mazo tenga cartas
    carta_del_mazo= mazo.pop(0) #sacamos la primera carta del mazo 
    print(f'Tu carta es {carta_del_mazo}') 
    if carta_anterior is not None and carta_anterior.split()[0]==carta_del_mazo.split()[0]:
        respuesta= input('¡Batalla! Quieres jugar? (si/no): ').lower()
        if respuesta=='si':
            puntos_jugador += 1
            print('¡Has ganado la batalla!')
        else:
            puntos_computadora+=1
            print("¡La computadora gana la batalla!")
    
    carta_anterior=carta_del_mazo
    mazo_barajado.append(carta_del_mazo)

#obtenemos los resultados del jueg
print("Resultados finales:")
print(f'Tus puntos: {puntos_jugador}')
print(f'Puntos de la computadora: {puntos_computadora}')

#obtenemos al ganador
if puntos_jugador > puntos_computadora:
    print(f'¡Felicitacioneds! Ganaste el juego con {puntos_jugador} pts')
elif puntos_jugador < puntos_computadora:
    print(f'¡La computadora ha ganado el juego con {puntos_computadora} pts!')
else:
    print("¡Es un empate!")