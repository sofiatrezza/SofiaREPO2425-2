"""
Desarrolla un programa que permita determinar si un número introducido por
consola es narcisista o no:
● Número narcisista: todo número de k dígitos que cumple que es igual a la
suma de las potencias k de sus dígitos es un número narcisista. Por ejemplo,
153 es un número narcisista de 3 dígitos, ya que 13+53+33=153.
"""

numero=int(input('ingrese un numero entero>>>'))
"""
el numero narcicista es aquel que la suma de sus digitos 
elevados a el numero de digitos es igual al mismo
"""
num_digitos=len(str(numero)) #conseguimos el numero de digitos casteando a str
num_feliz=False #asumimos que el numero no es narcicista
calculo=0 #llamamos un contador donde se almacenaran las potencias

#iteramos sobre los digitos del numero, casteando a str
for digito in str(numero):
    #al contador iremos sumando cada digido elevado al numero de digitos
    calculo += int(digito)**num_digitos #para poder elevar debemos castear a int

#planteamos el condicional
if calculo ==numero:
    num_feliz=True
    print(f'el numero {numero} es narcicista')
else:
    print(f'el numero {numero} no es narcicista')