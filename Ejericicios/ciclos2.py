#Realice un algoritmo que dado un número imprima su tabla de multiplicación 

print('Vamos a aprender las tablas de multiplicar!')
num=int(input('Ingrese un numero entero: '))

print(f'La tabla de multiplicar de {num} es: ')
for i in range(1,11):
    resultado=num*i
    print(f'{num} x {i} = {resultado}')
    