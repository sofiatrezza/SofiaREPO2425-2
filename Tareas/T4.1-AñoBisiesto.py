año= int(input('Introduzca un año entre 1900 y 2199: '))
if año>=1990 and año<=2199:
    pass
else:
    print('Introduzca un valor valido')
    año=int(input('Introduzca un año entre 1900 y 2199: '))
#definimos las variables de contador
contador_bisiesto=1
año_min=1900
#el año "tope" es el ingresado por el usuario
while año_min<=año:
    if año_min%4==0 and (año_min%100!=0 or año_min%400==0):
        contador_bisiesto += 1
    año_min +=1
#calculo del normal
diferencia=año-1900
año_normal=diferencia-contador_bisiesto

print("Entre 1900 y "+str(año)+' hay '+str(contador_bisiesto)+' años bisiestos y '+str(año_normal)+' años normales.')
