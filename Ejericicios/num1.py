"""
Escriba una función que tome una lista de números y devuelva la suma acumulada,
es decir, una nueva lista donde el primer elemento es el mismo, el segundo
elemento es la suma del primero con el segundo, el tercer elemento es la suma del
resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la
suma acumulada de [1,2,3] es [1, 3, 6].
"""

numeros=[1,2,3,4,5,6,7,8,9,10]

def suma_acumulada(numeros):
    #creamos una lista vacia donde colocaremos las sumas acumuladas
    lista_num_acum=[]
    #creamos el contador donde se iran almacenado las sumas
    suma=0
    #iteramos sobre la lista de numeros
    for numero in numeros:
        #empezamos, indice=0 >>> numero=1
        suma+=numero #suma=suma+numero (0+1=1)
        #se agrega el resultado de suma a la lista
        lista_num_acum.append(suma)
        """
        se repite el bucle- indice=1>>> numero 2
        suma= suma + numero= 1+2= 3
        se agrega suma=3 a la lista
        """
    return lista_num_acum

print(suma_acumulada(numeros))