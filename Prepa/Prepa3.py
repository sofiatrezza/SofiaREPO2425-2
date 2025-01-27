#desarrolle un algoritmo que determine si un numero es
#primo
#compuesto
#oblongo- un numero que es resultado de la multiplicacion de dos numeros seguidos 2x3=6
#palindromo- un num que se lee igual de derecha a izquierda y de izquierda a derecha
#perfecto- la suma de todos los divisores de un numero es igual al numero
#abundante- la suma de todos sus divisores es mayor al numero
#deficiente- la suma de todos sus divisores es menor al numero
#cuadrado
#no cuadrado


x=int(input('ingrese un numero: '))
#asumimos que el numero es primo
primo= True
#va a recorrer todos los numeros desde dos hasta el ingresado
#se toma a partir de 2 porque es el primer numero primo
for d in range(2,x):
    if x%d==0: #pobamos que sea divisible
        #si es divisible entonces primo, ya no es primo FALSE
        primo= False
        print(f'el numero {x} es compuesto')
        break

if primo:
    print(f'el numero {x} es primo')

for i in range(1, x): #todos los numeros desde el 0 hasta el numero que ingresa sin tomar ese numero
    if i*(i+1)==x:
        print(f'el numero {x} es oblongo')
        break #se rompe el ciclo si la condicion se cumple

#esto solo funciona para strings entonces los casteamos
aux=str(x)[::-1] #te voltea un string, para poder invertir es con -1
if x==int(aux):
    print(f'el numero {x} es palindromo')

divisores=0
for b in range(1, x):
    if x%b==0: #pobamos que sea divisible
        divisores+=b #sumamos el valor de su divisor
#no colocamos break porque queremos saber todos sus divisores

if divisores==x:
    print(f'el numero {x} es perfecto')
if divisores>x:
    print(f'el numero {x} es abundante')
else:
    print(f'el numero {x} es deficiente')

cuadrado= False
for c in range(x):
    if x==d**2:
        cuadrado= True
        print(f'el numero {x} es cuadrado')
        break

if not cuadrado:
    print(f'el numero {x} es libre de cuadrados')

cifras=list(str(x))
if len(set(cifras))<len(cifras):
    print(f'el numero {x} tiene cifras repetidas')
if len(set(cifras))==1:
    print(f'el numero {x} esta compuesto por una sola cifra')
