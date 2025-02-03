#tablas de multiplicar del 1 al 10

for i in range(1,11):
    print(f'Tabla de multiplicar del {i}')
    for m in range(1,11):
        mult=i*m
        print(f'{i} x {m} = {mult}')