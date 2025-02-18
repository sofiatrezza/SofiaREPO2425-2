"""
Sofia Trezza
Tarea 9- seccion 2
Cree un programa que permita registrar tres tipos de empleado (Profesor, Administrativo, Mantenimiento) 
y permita indicar que cada uno de ellos ha comenzado o terminado su jornada laboral. El efecto de comenzar 
la jornada para cada tipo de empleado debe ser diferente, pero debe usarse la misma llamada para hacerlo 
en todos los casos.
Trate de usar la herencia lo más posible.
"""

#definimos la clase empleado
class Empleado:
    #la clase esta definida por el nombre del empleado
    def __init__(self, nombre):
        self.nombre=nombre
        #creamos el atributo que indica que el empleado no ha iniciado su jornada
        self.jornada_iniciada=False

    #creamos el primer metodo de instancia para iniciar la jornada
    def iniciar_jornada(self):
        #si la jornada no ha iniciado entonces se le da inicio "True"
        #esto es para verificar si se inicio la jornada
        if not self.jornada_iniciada:
            self.jornada_iniciada= True
            return f'{self.nombre} ha comenzado su jornada laboral'
        else: #si es True entonces ya se habia iniciado
            return f'{self.nombre} ya ha inciado su jornada laboral'
    
    #creamos el metodo de instancia
    def terminar_jornada(self):
        #verificamos si ya esta iniciada la jornada
        if self.jornada_iniciada:
            self.jornada_iniciada= False
            return f'{self.nombre} ha terminado su jornada laboral'
        else: #si es False es porque no se inicio la jornada
            return f'{self.nombre} no ha iniciado su jornada laboral'
        
#creamos las subclases para el personal
class Profesor(Empleado):
    def iniciar_jornada(self):
        msj= super().iniciar_jornada()
        return msj

class Administrativo(Empleado):
    def iniciar_jornada(self):
        msj= super().iniciar_jornada()
        return msj

class Mantenimiento(Empleado):
    def iniciar_jornada(self):
        msj= super().iniciar_jornada()
        return msj
        

profesor = Profesor("Juan")
administrativo = Administrativo("Ana")
mantenimiento = Mantenimiento("Luis")

print(profesor.iniciar_jornada())  # Inicia la jornada del profesor
print(administrativo.iniciar_jornada())  # Inicia la jornada del administrativo
print(mantenimiento.iniciar_jornada())  # Inicia la jornada del mantenimiento

print(profesor.terminar_jornada())  # Termina la jornada del profesor
print(administrativo.terminar_jornada())  # Termina la jornada del administrativo
print(mantenimiento.terminar_jornada())  # Termina la jornada del mantenimiento