"""
 Un taxi cobra 5 dólares por los primeros 200 metros o fracción recorridos. A 
partir de allí cobra 2 dólares adicionales por cada 200 metros o fracción 
recorridos y así sucesivamente hasta llegar a 1.6 kilómetros que es cuando la 
tarifa se estabiliza. Como ejemplo, considere que 
a. 160 km son $5 
b. 320 km son $7 
c. 1599 km son $19 
d. 1600 km son $19 
Dé el diagrama de flujo e implemente el programa que solicita la distancia 
viajada e imprima el costo del viaje. 
"""
import math
print('Bienvenido, disfrue su viaje!')
print('Nuestros viajes ofrecen distancias: \nMinimo 200 m \nMaximo 1600 m o 1.6 km')
distancia=int(input('Ingrese la distancia recorrida en metros: '))
if distancia<200 or distancia>1600:
    print('La distancia excede el limite o es menor al minimo')
    distancia=int(input('Ingrese una distancia valida: '))

tarifa_inicial=5
monto=0

if distancia>200:
    metros_extra=distancia-200
    secciones_extra= math.ceil(metros_extra//200)
    monto+=secciones_extra*2
    costo=tarifa_inicial+monto
    print(f'El costo del viaje es de ${costo}')