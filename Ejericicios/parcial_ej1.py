"""
Pregunta 1 (6 puntos)
Realiza una función que reciba dos cadenas de texto: joyas y piedras.
 La cadena joyas representa los tipos de piedras que son, como su nombre lo indica, 
 joyas, y la cadena piedras representa todas las piedras que tú tienes que pueden ser de 
 cualquier clase, es decir joyas o no. Cada carácter en la cadena piedras es un tipo de 
 piedra que tú tienes. Haz un algoritmo que te ayude a saber cuántas de las piedras que tienes 
 también son joyas. Asume que las vocales abiertas (“a”, “e”, “o”) son joyas, mientras que las 
 vocales cerradas (“i”, “u”) así como las consonantes, son un tipo de piedra diferente a las joyas
- Input: joyas = "aae", piedras = "aiebbrb"
- Output: 3
- Explicación: las joyas son “a” y “e”; como tengo una “e” y dos “a” tengo 3 joyas
en total.

"""

#joyas= input('ingrese sus joyas>>> ')
#piedras= input('ingrese sus piedras>>> ')

joyas='aae'
piedras= 'aiebbrb'

def son_joyas(joyas, piedras):
    contador=0
    for piedra in piedras:
        for joya in joyas:
            if joya==piedra:
                contador+=1
    print(f'hay {contador} joyas')

print(son_joyas(joyas,piedras))