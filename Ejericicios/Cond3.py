# Una famosa cadena de cines en Venezuela te contrató para hacerles un programa de descuento 
#en las entradas basado en la edad del cliente, para ello tendrás que recibir por teclado la edad y 
#nombre del cliente y verificar los siguientes casos: 
#a. Si su edad es menor o igual a 4 años el precio de su entrada es gratis. 
#b. Si su edad es menor o igual a 18 años el precio de su entrada es de $1.50 
#c. Si su edad es mayor o igual a los 60 años su entrada tendrá un valor de $1 
#d. La entrada para un adulto promedio es de $2.00 
#Deberás imprimir un mensaje dependiendo de la edad del cliente para saber el precio de su 
#entrada. 
#Output: 'El cliente: {nombre} tiene: {edad} años y su entrada de cine cuesta: ${precio_entrada}'

print('Bienvenido a CINESMET, ingrese sus datos:')
nombre=str(input('Nombre: ')).capitalize()
apellido=str(input('Apellido: ')).capitalize()
edad=int(input('Edad: '))
entrada= 2
if edad<=4:
    entrada=0
if edad<=18:
    entrada=1.50
if edad>=60:
    entrada=1
print(f'El cliente {nombre} {apellido} tiene {edad} años y su entrada de cine cuesta ${entrada}.')
