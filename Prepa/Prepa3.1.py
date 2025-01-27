#sucesion de fibonacci

x=int(input('ingrese un numero >> '))
# este valor sera el tope de la sucesion, el maximo
sucesion= []

for i in range(x+1):
    if i==0:
        sucesion.append(i)
    elif i==1:
        sucesion.append(i)
    else:
        sucesion.append((i-1)+(i-2))

print(f'La Sucesion de Fibonacci de {x} es {sucesion}')