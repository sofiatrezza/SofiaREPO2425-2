#numeros pares
#variable de iteracion
num=1
usuario= int(input('Introduzca un numero: '))
while num<=usuario:
    #para que el programa no colapse se tiene que iterar la variable
    num+=1
    #si el numero es par (se lee como divisible entre dos) entonces el programa sigue
    if num%2==0:
        print('El numero '+str(num)+' es par')
        continue
    #se podria usar un print que indique el num del ciclo es par
    else:
        print('El numero'+str(num)+' es impar')
    #si no es par, entonces se imprime el numero
    