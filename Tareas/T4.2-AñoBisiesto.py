"""
Sofia Trezza
Seccion 2
Tarea 4- Sin bucles
"""

año= int(input('Introduzca un año entre 1900 y 2199: '))

if año<=1900 or año>=2199:
    print('Por favor introduzca un año entre 1900 y 2199 :)')
else:
    #se contabiliza la cantidad de años bisiestos manualmente
    años_divisible_entre_4=(año//4)-(1900//4)
    años_divisible_entre_100=(año//100)-(1900//100)
    años_divisible_entre_400=(año//400)-(1900//400)
    #se suma algebraicamente la cantidad de años bisiestos que hay realmente
    años_bisiestos=años_divisible_entre_4-años_divisible_entre_100+años_divisible_entre_400

    print(f"El número de años bisiestos que hay entre 1900 hasta {año} es {años_bisiestos}")