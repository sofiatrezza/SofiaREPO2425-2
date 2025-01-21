""""
Dadas tres variables enteras a, b y c con valores diferentes, determinar cuál es la suma máxima 
de dos de esas variables
"""
print('Calculemos la maxima suma entre las variables a, b y c')
a= int(input('Introduzca la variable a: '))
b= int(input('Introduzca la variable b: '))
c= int(input('Introduzca la variable c: '))

suma_ab= a+b
suma_bc= b+c
suma_ac= a+c
maxima_suma= suma_ab
if suma_bc>maxima_suma:
    maxima_suma=suma_bc
if suma_ac>maxima_suma:
    maxima_suma=suma_ac
print(f'La maxima suma entre las variables a, b y c es {maxima_suma}')
