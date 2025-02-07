'''
 Una marca de joyería que realiza sus ventas a través de Instagram realizará un sorteo que
 tendrá tres ganadores. Se sorteará la siguiente mercancía:
Primer lugar: 1 collar, 2 pulseras, 2 pares de zarcillos y 3 anillos.--
 Segundo lugar: 1 collar, 1 pulsera y 2 anillos.
 Tercer lugar: 1 pulsera y 1 par de zarcillos.
 Tu labor es diseñar para ellos un programa (con ayuda de la librería “random”) que, de todos
 los usuarios que están participando (de máximo 30 caracteres, recibidos como input y
 almacenados en una lista) seleccione a los 3 ganadores al azar e indique cuál fue el premio.
 Output:
 1er lugar: @{primer_ganador} ha ganado 1 collar, 2 pulseras, 2 pares de zarcillos y 3
 anillos.
 2do lugar: @{segundo_ganador} ha ganado 1 collar, 1 pulsera y 2 anillos.
 3er lugar: @{tercer_ganador} ha ganado 1 pulsera y 1 par de zarcillos.
 Nota: el módulo de registro de participantes y el de selección del ganador deben estar en
 dos archivos diferentes, en el main solo deben ejecutarse las funciones
'''

import random

participante=input('ingrese su usuario>>> ')
usuarios=[]
if len(participante)>30:
    print('el usuario debe tener maximo 30 caracteres')
    participante=input('ingrese su usuario correctamente>>> ')
else:
    usuarios.append(participante)
