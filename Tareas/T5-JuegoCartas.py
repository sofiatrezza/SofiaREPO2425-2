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

#definimos la variable para comparar con la carta anterior
carta_anterior=None 

#variable para guardar el mazo barajado
mazo_barajado=[]

print("¡Bienvenido al juego de Batalla!")
print("Presiona ENTER para sacar la siguiente carta")
print("SI crees que saldra el mismo valor que la carta anterior, escribe 'batalla' y luego presiona ENTER \n")

#empezamos el juego
while mazo: #mientras que el mazo tenga cartas
    #pedimos hacer una accion al usuario
    accion=input('Pulsa ENTER para sacar carta o escribe "batalla": ').strip().lower()
    #sacamos la siguiente carta del mazo 
    carta_del_mazo= mazo.pop(0) 
    
    #comparamos la carta actual con la carta anterior solo si existe
    if carta_anterior is not None:
        valor_anterior=carta_anterior.split()[0]
        valor_actual= carta_del_mazo.split()[0]

        #si se rrepiten los valores de la carta del mazo
        if valor_anterior== valor_actual:
            if accion == 'batalla':
                puntos_jugador += 1
                print('¡Has ganado la batalla!')
            else:
                puntos_computadora+=1
                print("¡La computadora gana la batalla!")
    
    #mostramos la carta
    print(f'Tu carta es {carta_del_mazo}')
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