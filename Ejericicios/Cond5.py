"""
Desarrolla en Python el juego de Piedra, Papel y Tijeras en donde pedirás por teclado la opción 
del jugador 1, luego la opción del jugador 2, y posteriormente dará el resultado diciendo quién ganó.
"""
print('Juguemos! Piedra, papel o tijera?')
jugador_a= str(input('Jugador a, piedra, papel o tijera?: ')).lower()
jugador_b= str(input('Jugador b, piedra, papel o tijera?: ')).lower()

if jugador_a==jugador_b:
    print('Empate!')
elif (jugador_a=="piedra" and jugador_b=="tijera") or\
    (jugador_a=="papel" and jugador_b=="piedra") or \
    (jugador_a=="tijera" and jugador_b=="papel"):
    print('Gana el Jugador a!')
else:
    print('Gana el Jugador b!')

