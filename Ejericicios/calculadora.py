"""
 Elabore una calculadora que reciba del usuario sus respectivos operandos, realice la
 operación correspondiente entre los mismos, almacene este resultado y no lo muestre
 hasta que el usuario lo desee mostrar en pantalla o eliminarlo para realizar otra
 operación. La calculadora deberá ser capaz de ofrecerle al usuario las siguientes operaciones:
Adición.----
 Sustracción.
 Multiplicación.
 División.
 Potenciación
"""

operando_1=int(input('ingrese el primer numero>>> '))
operando_2=int(input('ingrese el segundo numero>>> '))
operacion=input('ingrese la operacion que desea realizar (ej. 1):\
                \n1-Suma\
                \n2-Resta\
                \n3-Multiplicación\
                \n4-División\
                \n5-Potenciación\
                \n>>> ')

if int(operacion)==1:
    suma=operando_1+operando_2
    print(suma)
elif int(operacion)==2:
    resta=operando_1-operando_2
    print(resta)
elif int(operacion)==3:
    multiplicacion=operando_1*operando_2
    print(multiplicacion)
elif int(operacion)==4:
    division=operando_1/operando_2
    print(division)
else:
    potenciacion=operando_1**operando_2
    print(potenciacion)