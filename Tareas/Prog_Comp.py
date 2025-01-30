palabras=['vaquera','whiskey','gorra','mexico','rally']

def nativa(palabras):
    foraneos=['k','w','x','y']
    list=[]
    for palabra in palabras:
        for letra in palabra:
            if letra not in foraneos:
                list.append(palabra)
                return(list)

print(nativa(palabras))
