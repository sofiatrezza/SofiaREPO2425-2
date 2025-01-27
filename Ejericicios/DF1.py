"""
Tres valores son las longitudes de un triángulo no-degenerado si, y solo si, un 
lado es menor que la suma de los otros dos y mayor que su diferencia. Un 
triángulo es equilátero si sus tres lados son iguales, isósceles si dos lados son 
iguales y uno es desigual y escaleno si tres lados son desiguales. 
Haga el diagrama de flujo e implemente un programa que, dados tres números 
enteros, determine si estos 
a. forman un triángulo 
b. qué tipo de triángulo forma (es decir, si es equilátero, escaleno o 
isósceles)
"""
#solicitamos al usuario 3 numeros
print('Por favo introduzca 3 numeros enteros para cada variable a continuacion!')
lado_a=int(input('Introduzca un numero que se asiganara a un lado del triangulo: '))
lado_b=int(input('Introduzca otro numero que se asiganara a otro de los lados del triangulo: '))
lado_c=int(input('Introduzca un ultimo numero que se asiganara al ultimo lado del triangulo: '))

suma=lado_a+lado_b
diferencia=abs(lado_a-lado_b)

#desarrollamos un ciclo que determine que si se cumple que es un triangulo y luego se revisa su tipo
while lado_c<suma and lado_c>diferencia:
    if lado_a==lado_b==lado_c:
        print('El triangulo es equilatero, todos sus lados son iguales.')
    if lado_a==lado_b or lado_a==lado_c or lado_b==lado_c:
        print('El triangulo es isosceles, dos de sus lados son iguales.')
    else:
        print('El triangulo es escaleno, todos sus lados son diferentes.')
    quit()