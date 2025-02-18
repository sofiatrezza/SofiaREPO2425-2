
"""
Realiza una función que reciba un arreglo prices donde prices[i] es el precio de una acción 
dada en el día i. Quieres maximizar tu beneficio eligiendo un solo día para comprar una acción 
y otro día en el futuro para vender esa acción. Devuelve el beneficio máximo que puedes obtener 
de esta transacción. Si no puedes obtener ningún beneficio, devuelve 0.
-	Input:  prices = [7,1,5,3,6,4]
-	Output: 5
-	Explicación: Compra en el día 2 (precio = 1) y vende en el día 5 (precio = 6), beneficio = 6-1 = 5.
-	Nota: Comprar en el día 2 y vender en el día 1 no está permitido porque debes comprar antes de vender.

"""

prices = [7,1,5,3,6,4]
def beneficio_maximo(prices):
    beneficios=[]
    for dia_compra in range(len(prices)):
        for dia_venta in range(dia_compra+1, len(prices)):
            beneficios.append(prices[dia_venta]-prices[dia_compra])

    beneficio_max= f'el beneficio maximo que se puede obtener es {max(beneficios)}'
    return beneficio_max

print(beneficio_maximo(prices))
