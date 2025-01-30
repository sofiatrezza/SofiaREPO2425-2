"""
 Diseña un algoritmo que clasifique los números de la lista dada en las categorías correspondientes:
 numeros = [1634, 225, 490, 9926315, 800, 93084, 313, 216, 864, 757, 243, 301, 833, 200, 54748, 32, 787,
 536, 343, 353, 24678050, 16, 370, 181, 131, 818, 24678051, 153, 196, 400, 784, 31, 371, 9474, 10301, 729, 648,
 973, 256, 548834, 9800817, 9, 289, 302, 81, 101, 36, 716, 968, 100, 49, 432, 169, 484, 128, 125, 961, 1000,
 608, 219, 739, 529, 797, 931, 27, 108, 379, 727, 324, 121, 841, 288, 373, 919, 92727, 8208, 64, 632, 625,
 4210818, 144, 1741725, 72, 151, 929, 675, 790, 655, 11, 407, 512, 25, 262, 900, 383, 441, 392, 576, 7, 361, 972,
 88593477, 500, 676, 191, 1597, 7951]
 ● Número feliz:un número es feliz cuando cumple que si sumamos los cuadrados de sus
 dígitos y seguimos el proceso con los resultados de esas sumas que vamos obteniendo en
 cada paso, el resultado final, cuando llegamos a una suma con un solo dígito, es 1. Por
 ejemplo, el número 203 es un número feliz ya que 4+0+9=13; 1+9=10; 1+0=1.
 ● Número narcisista:todo número de k dígitos que cumple que es igual a la suma de las
 potencias k de sus dígitos es un número narcisista. Por ejemplo, 153 es un número narcisista
 de 3 dígitos, ya que 13+53+33=153.
 ● Númeropalíndromo:número natural que se lee igual de derecha a izquierda y de izquierda
 a derecha. Por ejemplo 1348431
"""

numeros = [1634, 225, 490, 9926315, 800, 93084, 313, 216, 864, 757, 243, 301, 833, 200, 54748, 32, 787,
 536, 343, 353, 24678050, 16, 370, 181, 131, 818, 24678051, 153, 196, 400, 784, 31, 371, 9474, 10301, 729, 648,
 973, 256, 548834, 9800817, 9, 289, 302, 81, 101, 36, 716, 968, 100, 49, 432, 169, 484, 128, 125, 961, 1000,
 608, 219, 739, 529, 797, 931, 27, 108, 379, 727, 324, 121, 841, 288, 373, 919, 92727, 8208, 64, 632, 625,
 4210818, 144, 1741725, 72, 151, 929, 675, 790, 655, 11, 407, 512, 25, 262, 900, 383, 441, 392, 576, 7, 361, 972,
 88593477, 500, 676, 191, 1597, 7951]

felices=[]
narcisista=[]
palindromo=[]

num_feliz=False
num_narcisista= False
# Iteraramos sobre cada número en la lista
for numero in numeros:
    vistos = set()   # Creamos un conjunto para almacenar números ya vistos
    original = numero #guardamos el numero original en una variable para meterlo en la lista
    
    # Calculamos si el número es feliz, tomando en cuenta que el numero no puede ser 1
    # y no puede estar en la lista de vistos
    while numero != 1 and numero not in vistos:
        #si no se cumple, se agrega el num a vistos
        vistos.add(numero)
        # si no sumar los cuadrados de los dígitos
        numero = sum(int(digito) ** 2 for digito in str(numero))
    
    # Clasificar el número según el resultado
    if numero == 1:
        felices.append(original)
    

# Imprimir resultados
print("Números felices:", felices)
