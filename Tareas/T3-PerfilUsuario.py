#Creacion perfil de usuario
print('Bienvenid@ al curso de Algoritmos y Programacion 2425-2')
nombre_usuario= input('Introduzca su nombre: ')
if nombre_usuario[0].isupper():
    print('Hola '+nombre_usuario+'!')
else:
    nombre_usuario=nombre_usuario.capitalize()
    print('Hola '+nombre_usuario+'!')

#definimos el sexo
sexo= input('Sexo: Femenino o Masculino: ').lower()
if sexo=='femenino':
    print('Bienvenida, responde a las siguientes preguntas:')
    region=int(input(nombre_usuario+', cual es tu region favorita entre... \n1. Venezuela \n2. Barcelona \n3. Italia \nSeleccione entre 1, 2 o 3 \n:  '))
    if region==1:
        cosa_fav=input('Cual es tu cosa favorita de Venezuela... \nHallacas \nEmpanada \nPabellon \n: ').lower()
        print('Increible '+nombre_usuario+'!, '+cosa_fav+' tambien es mi cosa favorita')
    elif region==2:
        cosa_fav=input('Cual es tu cosa favorita de Barcelona... \nBikini (Sandwich de Jamon) \nVino \nCanelones \n: ').lower()
        print('Increible '+nombre_usuario+'!, '+cosa_fav+' tambien es mi cosa favorita')
    elif region==3:
        cosa_fav=input('Cual es tu cosa favorita de Italia... \nPasta \nPizza \nPanini \n: ').lower()
        print('Increible '+nombre_usuario+'!, '+cosa_fav+' tambien es mi cosa favorita')
    else:
        print('Por favor ingresa una opcion valida')

elif sexo=='masculino':
    print('Bienvenida, responde a las siguientes preguntas:')
    region=int(input(nombre_usuario+', cual es tu region favorita entre... \n1. Venezuela \n2. Barcelona \n3. Italia \nSeleccione entre 1, 2 o 3 \n:  '))
    if region==1:
        cosa_fav=input('Cual es tu cosa favorita de Venezuela... \nHallacas \nEmpanada \nPabellon \n: ').lower()
        print('Increible '+nombre_usuario+'!, '+cosa_fav+' tambien es mi cosa favorita')
    elif region==2:
        cosa_fav=input('Cual es tu cosa favorita de Barcelona... \nBikini (Sandwich de Jamon) \nVino \nCanelones \n: ').lower()
        print('Increible '+nombre_usuario+'!, '+cosa_fav+' tambien es mi cosa favorita')
    elif region==3:
        cosa_fav=input('Cual es tu cosa favorita de Italia... \nPasta \nPizza \nPanini \n: ').lower()
        print('Increible '+nombre_usuario+'!, '+cosa_fav+' tambien es mi cosa favorita')
    else:
        print('Por favor ingresa una opcion valida')
   
else:
    print('La respuesta no es valida, tomar una opcion entre femenino o masculino, o revisar ortografia')
    