cocacola = [80,100,93,99,101,102,95,110,109,120,125,130]

def rallies(cocacola):
  contador=0
  rally=[]
  #revisando todos los indices de la lista desde el segundo elemento hasta el ultimo
  for indice in range(1, len(cocacola)): 
      #si el elemento en el indice i=1 es mayor al que esta en el indice i-1=1-1=0
      if cocacola[indice]>cocacola[indice-1]:
          #entonces se aumenta el contador
          contador+=1
      else:
          #si no, se agrega el contador obtenido a la lista
          rally.append(contador)
          #y el contador se reinicia
          contador=0
  return max(rally) #max para que se ponga el maximo contador- si rally=[1,3,1] entonces es 3
    
print(rallies(cocacola))   
