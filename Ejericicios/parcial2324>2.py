"""
Hay “n” niños con caramelos. Se te da un arreglo de enteros candies, donde cada candies[i] 
representa el número de caramelos que tiene el niño i, y un entero extra_candies, que denota
 el número de caramelos extra que tienes. Devuelve un arreglo booleano result de longitud n, 
 donde result[i] es verdadero si, después de darle todos los extra_candies al niño i-ésimo, 
 este tendrá el mayor número de caramelos entre todos los niños, o falso de lo contrario. 
 Nota que varios niños pueden tener el mayor número de caramelos.

-	Input: candies = [2,3,5,1,3], extra_candies = 3
-	Output: [True, True, True, False, True] 
-	Explicación: Si das todos los extra_candies a:
-	Niño 1, tendrá 2 + 3 = 5 caramelos, que es el mayor número entre los niños.
-	Niño 2, tendrá 3 + 3 = 6 caramelos, que es el mayor número entre los niños.
-	Niño 3, tendrá 5 + 3 = 8 caramelos, que es el mayor número entre los niños.
-	Niño 4, tendrá 1 + 3 = 4 caramelos, que no es el mayor número entre los niños.
-	Niño 5, tendrá 3 + 3 = 6 caramelos, que es el mayor número entre los niños.

"""

candies = [2,3,5,1,3]
extra_candies = 3

def maximo_caramelos(candies, extra_candies):
    max_candy= max(candies)

    for i in range(len(candies)):
        if candies[i]+extra_candies>= max_candy:
            print(True)
        elif candies[i]+extra_candies<= max_candy:
            print(False)

print(maximo_caramelos(candies,extra_candies))
