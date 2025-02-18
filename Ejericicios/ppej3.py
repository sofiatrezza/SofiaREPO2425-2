"""
Supongamos que eres un padre increíble y quieres darle algunas galletas a tus 
hijos. Pero debes darle a cada niño a lo sumo una galleta. El i-ésimo niño tiene un 
factor de gula g[i], que es el tamaño mínimo de una galleta con la que el niño estará 
contento; y la j-ésima galleta tiene un tamaño s[j]. Si s[j] >= g[i], podemos asignar la j
ésima galleta al i-ésimo niño, y el niño estará contento. Tu objetivo es realizar una 
función que maximice el número de niños contentos y devuelva el número máximo. - - - - - - 
Input: g = [1,2,3], s = [1,1] 
Output: 1 
Explicación:  
Tienes 3 hijos y 2 galletas. Los factores de "gula" de los 3 hijos son 1, 2, 
3. Y aunque tienes 2 galletas, como su tamaño es 1, solo podrías hacer 
feliz al hijo cuyo factor de "gula" es 1. Necesitas devolver 1. 
Input:  g = [1,2], s = [1,2,3] 
Output: 2  
Explicación: Tienes 2 hijos y 3 galletas. Los factores de "gula" de los 2 
niños son 1, 2. Tienes 3 galletas y sus tamaños son lo suficientemente 
grandes como para satisfacer a todos los niños. Necesitas devolver 2. 
"""

g = [1,2]
s = [1,2,3]

def cuantas_devolver(g,s):
    for i in range(len(g)):
        for j in s:
            if g[i]==j:
                galleta=j
 
    return galleta

x= cuantas_devolver(g,s)
print(x)