#Te contrataron para realizar un programa donde calcule el premio de un juego. Los premios son 
#basados en puntos: 
#a. 1-50 No hay premio 
#b. 51-150 Bronze 
#c. 151-180 Plata 
#d. 181-200 Oro 
#Todos los límites inferior y superior aquí son inclusivos, y los puntos solo pueden tomar valores 
#enteros positivos hasta 200. En su declaración if, asigne la variable de resultado a un String que 
#contenga el mensaje apropiado según el valor de los puntos. 
#Si ganaron un premio, el mensaje debería decir: 
#Output:  "Felicitaciones, Ganaste la medalla de {nombre del premio} por haber tenido {puntos} pts!" 
#Si no hay premio, el mensaje debe decir: Output:  "No hay premios para {puntos} pts"

print('Hola! Bienvenido a Juego Land!')
puntos=int(input('Ingresa los puntos que ganaste para obtener tu premio: '))
#verificaciones
if puntos>200:
    puntos=int(input('El valor maximo son 200 puntos, ingrese su puntaje correcto: '))

premio='No hay premio'
if puntos>=1 and puntos<=50:
    print(f'Lo siento, {premio} para {puntos} pts :(')
if puntos>=51 and puntos<=150:
    premio='bronze'
    print(f'Felicitaciones! Ganaste la medalla de {premio} por haber tenido {puntos} pts!')
if puntos>=151 and puntos<=180:
    premio='plata'
    print(f'Felicitaciones! Ganaste la medalla de {premio} por haber tenido {puntos} pts!')
if puntos>=181:
    premio='oro'
    print(f'Felicitaciones! Ganaste la medalla de {premio} por haber tenido {puntos} pts!')

