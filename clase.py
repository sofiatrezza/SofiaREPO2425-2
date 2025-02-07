class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.velocidad=0
    
    def show_attr(self):
        return "Marca:{}, Modelo:{}, Color:{}, Velocidad:{}"\
                    .format(self.marca,self.modelo,self.color,self.velocidad)

    def acelerar(self, incremento):
        self.velocidad+=incremento
    
    def frenar(self, decremento):
        self.velocidad-=decremento
    
    def get_velocidad(self):
        return self.velocidad
    

    
jeep= Vehiculo("Jeep","Cherokee KK","Blanco")
jeep.acelerar(50)
print(jeep.show_attr())
