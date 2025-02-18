"""
Dado una lista de probabilidades donde cada elemento representa la probabilidad de lluvia de ese dia, 
escruba una funcion aumento_maximo que devvuelva otra lista donde el valor en cada posicion i
indique la diferencia entre el valor actual, el valor mas bajo precedente. Si no existe un valor mas
bajo precedente, el valor en esta prosicion es cero.
- Input: prob=[35,40,30,50]
- Output: [0,5,0,20]
"""

prob=[35,40,30,50]


lista_prob=[]
for i in range(len(prob)):
    minimo_precedente=float('inf')
    for j in range(i):
        if prob[j]<minimo_precedente:
            minimo_precedente=prob[j]
        else:
            minimo_precedente=float('inf')

    if minimo_precedente==float('inf'):
        diferencia=0
        lista_prob.append(diferencia)
    else:
        diferencia= abs(prob[i]-minimo_precedente)
        lista_prob.append(diferencia)

print(lista_prob)