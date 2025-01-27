#programa para determinar si un numero es primo

print('Determinemos si un numero es primo.\nUn numero primo es aquel que solo es divisible entre 1 y si mismo')
print('Por ejemplo, el numero 2, solo es divisible entre 1 y entre el mismo :)')
print('Pd. el 0 y el 1 no son numeros primos')

#se le pide al usuario que ingrese un numero
num=int(input('Ingrese un numero mayor que 2: '))
if num<2: #se verifica que este numero sea mayor que 2, porque el 0 y 1 no son primos
   num(int(input('Ingrese un numero mayor que 2: ')))

#se va a tomar el 2 como el primer divisor ya que
divisor=2
#asumiendo que el numero es primo
es_primo= True

#si un número tiene un divisor mayor que su raíz cuadrada, 
#necesariamente tendrá otro divisor menor que ella.  
#solo necesitamos comprobar hasta la raíz cuadrada del número.
while divisor*divisor<=num:
    #se comprueba a ver si es divisible entre el divisor
    if num%divisor==0:
        es_primo= False
        print(f'El numero {num} no es primo') #si es dividible, entonces ya no es primo
        break # salimos del ciclo si encontramos un divisor
    divisor+=1 #se aumenta el contador para seguir probando en caso que no se haya encontrado un multiplo
       
if es_primo:
    print(f'El numero {num} es primo :)')