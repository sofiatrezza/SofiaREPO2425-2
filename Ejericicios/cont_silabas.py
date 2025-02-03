"""
Se tienen tres textos almacenados en tres variables como strings. Para cada texto debes
 contar cuántas veces se repite la sílaba indicada y qué índice ocupa cada repetición.--
y: “om”
 z: “in”
"""

x = "Outside of that, Hu argues that the royalties can be more reliable than\
the entropy of Wall Street. No matter what happens to the stock market, people\
are always going to be listening to music."
y = "CBD, which comes from either a marijuana or hemp plant, is\
non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol).\
It may, however, offer anti-inflammatory, antioxidant, anti-psychotic,\
anti-convulsant, and antidepressant properties. Because it can hemp is legal\
in all 50 states, hemp-derived CBD products are becoming more readily\
available online and in stores all over the country."
z = "According to a report published by Fast Company, apparel sales have\
plummeted by 50 percent. It’s a margin that will be difficult to recover from,\
especially for small businesses that don’t have the backing of major\
conglomerates. These independent companies rely on seasonal buys from\
retailers to stay afloat. But with the bevy of store closures and restrictions\
on online sales, these behemoth retailers are facing hard times of their own."

silaba_x='at'
silaba_y='om'
silaba_z='in'
index_x=[]
index_y=[]
index_z=[]

def encuentra_silaba_x(x, silaba_x,index_x):
    inicio=0
    while True:
        inicio=x.find(silaba_x,inicio)
        if inicio==-1:
            break
        index_x.append(f'{inicio}-{inicio+1}')
        inicio+=1
    print(f'la silaba {silaba_x} se repite {len(index_x)} veces en los indices\n{index_x}')

print(encuentra_silaba_x(y,silaba_y,index_y))
print(encuentra_silaba_x(x,silaba_x,index_x))
print(encuentra_silaba_x(z,silaba_z,index_z))
