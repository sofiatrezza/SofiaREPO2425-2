numero=int(input('ingrese un numero>>> '))

factorial=1
for i in range(1,numero+1):
    factorial*= i
    
print(f'el factorial de {numero} es {factorial}')