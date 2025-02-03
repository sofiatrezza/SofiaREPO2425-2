"""
Dado un entero X de tres dígitos diferentes, imprima "SÍ" si sus tres dígitos van en orden
ascendente de izquierda a derecha e imprima "NO" de lo contrario.
"""

numero=int(input('ingrese un numero de 3 cifras>>> '))
if numero>=100 and numero<=999:
    pass
else:
    numero=int(input('por favor ingrese un numero de 3 cifras>>> '))

for digitos in str(numero):
    if int(digitos)+1>int(digitos) and int(digitos)>int(digitos)-1:
        print('SI')
    else:
        print('NO')
