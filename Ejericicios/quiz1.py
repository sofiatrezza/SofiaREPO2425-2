"""
Crea un módulo para validación de contraseña. Dicho módulo deberá cumplir
con los siguientes criterios de aceptación
La contraseña debe tener:
-Mínimo de 8 caracteres
-Debe contener letras minúsculas, mayúsculas, números y al menos 1 caracter no alfanumérico
-No puede contener espacios en blanco
"""

key=input('Por favor cree una contraseña\nLa contraseña debe tener mínimo de 8 caracteres\nDebe contener letras minúsculas, mayúsculas, números y al menos 1 caracter no alfanumérico\nNo puede contener espacios en blanco\n>>>')

if len(key)<8:
    print('La contraseña debe tener minimo 8 caracteres')
    key=('Ingrese una contraseña valida: ')

if ' ' in key:
    print('La contraseña no debe tener espacios en blanco')
    key=('Ingrese una contraseña valida: ')

tiene_minuscula=False #si encuentra al manos una minuscula "any" devuelve True
tiene_mayuscula=False
tiene_numeros=False
no_tiene_alfanum=False

for k in key:
    if k.islower():
        tiene_minuscula= True
    elif k.isupper():
        tiene_mayuscula= True
    elif k.isdigit():
        tiene_numeros= True
    elif not k.isalnum(): # .isalnum() es True cuando todos los caracteres son especiales
        # es False cuando hay al menos un caracter especial, por eso ponemos not
        no_tiene_alfanum= True

if tiene_minuscula and tiene_mayuscula and tiene_numeros and no_tiene_alfanum == True:
    print('Contraseña ingresada correctamente')
else:
    print('La contraseña elegida no es valida')