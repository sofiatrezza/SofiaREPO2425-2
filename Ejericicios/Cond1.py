
numero=float(input('Introduzca un numero decimal (colocar ".") \npuede ser positivo o negativo :)\n'))

par_impar= "par" if numero%2==0 else "impar"
positivo_negativo= 'positivo' if numero>0 else "negativo"
print(f"El numero es {par_impar} y es {positivo_negativo}. \nPd. Ningun numero con decimales es par :)")
