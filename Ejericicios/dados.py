"""
 Con dos dados, al azar, se pueden obtener números entre 2 y 12 de varias formas. Crea un
 programa que reciba por teclado un número entre 2 y 12 y retorne las combinaciones posibles
 de números para que su suma sea igual al número ingresado (no debe repetirse la
 combinación, por ejemplo, 4-5 y 5-4 debe mostrarse solo una vez).
 Ejemplos de output:
Combinaciones para 5:
 * 1-4
 * 2-3
Combinaciones para 9:
 * 3-6
 * 4-5
"""


combinaciones=[]
numero= int(input('ingrese un numero entero entre 2 y 12 >>> '))
if numero<2 or numero>12:
    numero=int(input('por favor ingrese un numero valido>>> '))
else:
    pass

for dado_1 in range(1,7):
    for dado_2 in range(1,7):
        if dado_1+dado_2==numero:
            #se hace para evitar repeticiones
            if dado_1<=dado_2:
                combinaciones.append((dado_1,dado_2))
print(f'las combinaciones posibles para obtener el el numero {numero} son:')
for combo in combinaciones:
    print(combo)
