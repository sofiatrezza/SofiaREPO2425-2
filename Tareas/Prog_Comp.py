palabras=['vaquera','whiskey','gorra','mexico','rally']
foraneos=['k','w','x','y']

def nativa(palabras):
    for f in foraneos:
        for palabra in palabras:
            if f in palabra:
                palabras.remove(palabra)

    return palabras

print(nativa(palabras))