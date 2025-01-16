#se define la variable que va a arrojar el factorial de un numero
factorial=1
num=int(input("Introduzca un numero: "))
#se define la variable que va a iterar en el ciclo
count=1

#definimos el ciclo
#factorial de 3=3*2*1
while count<=num:
    #mientras que el contador sea menor al numero del usuario
    #se multiplica el contador por el factorial (primer numero es 1)
    #y se redefine la variable factorial a (pimer ciclo 1*1=1)
    factorial*=count
    #se aumenta el contador (iterando)
    count+=1
    #ahora 1+1=2 y se redefine el contador a 2
    #el prog va a multiplicar el contador por el factorial nuevamente y se va a ir obteniendo el factorial
    #se repite hasta que el contador sea igual al numero del usuario

print(factorial)