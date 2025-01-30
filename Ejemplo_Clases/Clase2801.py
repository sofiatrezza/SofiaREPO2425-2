#funciones - def

#se necesita un parametro para saber que es lo que tiene que hacer- esta proporciona un resultado
#python tiene funciones creada y nosotros podemos crear las nuestras con def

def volumen_cilindro(altura,radio):
    pi=3.14159
    return altura * pi * radio**2
print(volumen_cilindro)

x= volumen_cilindro(10,3)
print(x)
#>>> 282.7431

#solucion a replicacion de codigo
#cuando estoy haciendo algo varias veces, hago una funcion

