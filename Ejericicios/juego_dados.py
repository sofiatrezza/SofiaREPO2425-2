"""
 Realice un algoritmo que simule un juego de dados entre 2 jugadores, la idea de este
 juego obtener más puntos que el oponente, los mismos tendrán 7 turnos cada uno. El
 sistema de puntuación en los marcadores de cada jugador se verá reflejado por la cara del
 dado en el siguiente formato, si el dado después de lanzarlo tiene el valor de
1 +10 puntos
2 +20 puntos
3 Vuelve a lanzar (sin que cuente como turno).
4 Puntuación X2
5 +40 puntos
6 Puntuación /2
"""

import random

def juego_dados(puntuacion):
    intentos=0
    max_intentos=7
    while intentos<=max_intentos:
        dado= random.randint(1,6)
        if dado==1:
            puntuacion+=10
            intentos+=1
            print('+10 puntos')
        elif dado==2:
            puntuacion+=20
            intentos+=1
            print('+20 puntos')
        elif dado==3:
            print('intentalo de nuevo ;)')
        elif dado==4:
            puntuacion=puntuacion*2
            intentos+=1
            print('duplicaste tu puntuacion :)')
        elif dado==5:
            puntuacion+=40
            intentos+=1
            print('+40 puntos')
        else:
            puntuacion=puntuacion//2
            intentos+=1
            print('puntuacion a la mitad :(')
    return puntuacion

puntuacion_1=0
puntuacion_2=0
print('juguemos con dados')
print('es el turno del jugador 1!')
jugador_1=juego_dados(puntuacion_1)
print('es turno del jugador 2!')
jugador_2=juego_dados(puntuacion_2)

if jugador_1>jugador_2:
    print(f'el ganador es el jugador 1 con {jugador_1} puntos')
else:
    print(f'el ganador es el jugador 2 con {jugador_2} puntos')
