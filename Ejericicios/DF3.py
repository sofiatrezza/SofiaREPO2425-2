"""
 Realice el diagrama de flujo e implemente un programa que, dado un precio y 
un pago menores o iguales que $50, determinar el vuelto que se debe entregar 
si se utilizan billetes de $20, $10, $5, $2 y $1. Suponga que hay cantidades 
ilimitadas de billetes para dar vuelto. 
"""
print('Bienvenido a Tesco')
precio=float(input('Ingrese el precio del producto ($): '))
pago=float(input('Ingrese el monto a cancalar (Debe ser menor o igual a $50): '))
vuelto=pago-precio

billete_20=0
billete_10=0
billete_5=0
billete_2=0
billete_1=0

while vuelto>=20: #mientras que sean mas de $20 entonces se suma un billete de 20 
    billete_20+=1
    vuelto-=20 #se resta $20 ya abonado al vuelto y se revisa nuevamente

#si ya es menos que $20 entra en otro ciclo y asi sucesivamente
while vuelto>=10:
    billete_10+=1
    vuelto-=10
while vuelto>=5:
    billete_5+=1
    vuelto-=5
while vuelto>=2:
    billete_2+=1
    vuelto-=2
while vuelto>=1:
    billete_1+=1
    vuelto-=1

resultado= f'El vuelto a entregar es de: \n'
resultado+= f'{billete_20} billetes de $20\n'
resultado+= f'{billete_10} billetes de $10\n'
resultado+= f'{billete_5} billetes de $5\n'
resultado+= f'{billete_2} billetes de $2\n'
resultado+= f'{billete_1} billetes de $1\n'

print(f'Gracias por su compra!\nTotal= ${precio}\nCancelado= ${pago}\n{resultado}')