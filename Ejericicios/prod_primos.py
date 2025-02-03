"""
 Realice un algoritmo que dado un número N cualquiera, encuentre dos números
 primos A y B que al ser multiplicados resulte el número N. De no existir ningunos números
 A y B que cumplan la condición, el algoritmo deberá imprimir un mensaje de error.
"""

numero=int(input('ingrese un numero>>> '))
lista_primos=[]

def primo(num):
    if num<2:
        return False
    for i in range(1, (int(num)**2)+1):
        if num%i==0:
            return False
    return True
    

def producto_primos(numero):
    for a in range(2,numero):
        if primo(a):
            for b in range(2,numero):
                    if primo(b) and a*b==numero:
                        return a,b
    return None

resultado=producto_primos(numero)
if resultado:
    print(f'{numero} es resultado de la multiplicacion de {a}*{b}')
else:
    print(f'Error, no se encontraron 2 numeros primos que multiplicados resulten {numero}')
