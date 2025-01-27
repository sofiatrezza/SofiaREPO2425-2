"""
Sofia Trezza
Sección 2
Tarea 6

Haga un programa que permita jugar una batalla pokémon. En una batalla, 
cada jugador tiene un pokémon que conoce 4 ataques, de los cuales algunos 
son conocidos por ambos pokémon. Suponga que cada ataque tiene una cantidad de 
daño físico y una cantidad de daño a la defensa (es decir, puede cambiar el multiplicador de daño). 
Almacene esta información en uno o más diccionarios.
Permita al jugador escoger uno de los ataques y luego elija uno al azar para la computadora 
usando el módulo randomLinks to an external site. de Python.
Repita hasta que la cantidad de daño físigo agote los puntos de salud de alguno de los pokémones 
y declare el ganador.
Si tienen problemas para especificar cuáles ataques bajan los puntos de salud y cuáles bajan 
la defensa, recuerden que el diccionario puede ser una estructura de datos combinada.
"""

import random

# Creamos un diccionario con cada pokemón y sus ataques
pokemons = {
    "Pikachu": {
        "salud": 100,
        "ataques": {
            "Impactrueno": {"daño_físico": 20, "daño_defensa": 0.9},
            "Rayo": {"daño_físico": 25, "daño_defensa": 0.8},
            "Cola Ferrea": {"daño_físico": 15, "daño_defensa": 1.0},
            "Chispazo": {"daño_físico": 30, "daño_defensa": 0.7}
        }
    },
    "Charmander": {
        "salud": 100,
        "ataques": {
            "Llamarada": {"daño_físico": 25, "daño_defensa": 0.9},
            "Ascuas": {"daño_físico": 20, "daño_defensa": 1.0},
            "Garra Dragon": {"daño_físico": 30, "daño_defensa": 0.85},
            "Fuego Fatuo": {"daño_físico": 15, "daño_defensa": 1.1}
        }
    }
}

print("¡Bienvenido a la batalla Pokémon!")

# Se selecciona el Pokemon para cada uno, con el diccionario
pokemon_jug = pokemons["Pikachu"]
pokemon_comp = pokemons["Charmander"]

#se hace la condicion de que la salud no este en cero, es decir, que siga vivo
while pokemon_jug["salud"] > 0 and pokemon_comp["salud"] > 0:
    # se muestra los puntos que quedan de salud de cada jugador
    print(f"\nSalud de Pikachu: {pokemon_jug['salud']} | Salud de Charmander: {pokemon_comp['salud']}")
    
    # se muestran los ataques disponibles
    print("Ataques disponibles:")
    for ataque in pokemon_jug["ataques"]:
        print(f"- {ataque}")
    
    # se hace un input para elegir ataque del jugador
    ataque_jugador = input("Elige un ataque: ").capitalize()
    #se hace un ciclo para garantizar que el ataque exista
    while ataque_jugador not in pokemon_jug["ataques"]:
        print("Ataque no válido. Inténtalo de nuevo.")
        ataque_jugador = input("Elige un ataque: ").capitalize() #usamos capitalize para que seleccione el value
    
    # calculamos el daño del jugador
    # se accede al valor asociado al ataque elegido en el diccionario
    # se multiplica por el modificador de defensa asociado al ataque elegido
    # ej. impactrueno (daño físico= 20; defensa=0.9) entonces el jugador causó (20*0.9)=18 puntos de ataque contra el oponente
    daño_jug = pokemon_jug["ataques"][ataque_jugador]["daño_físico"] * pokemon_jug["ataques"][ataque_jugador]["daño_defensa"]
    pokemon_comp["salud"] -= daño_jug #actulizamos los puntos de salud de la comp= 100-18=82 pts
    print(f"Pikachu usó {ataque_jugador} y causó {daño_jug:.2f} puntos de daño.")
    #::.2f es para que python muestre una cantidad especifica de 2 decimales

    if pokemon_comp["salud"] <= 0: #Los ataques de Pikachu fueron mas fuertes
        print("¡Has ganado la batalla!")
        break

    # luego de que jug ataque, es turno de la computadora
    ataque_comp = random.choice(list(pokemon_comp["ataques"].keys())) #le pedimos a python que tome un ataque cualquiera del diccionario
    # calculamos el daño de la computadora al igual que antes
    daño_comp = pokemon_comp["ataques"][ataque_comp]["daño_físico"] * pokemon_comp["ataques"][ataque_comp]["daño_defensa"]
    # actualizamos los puntos de salud del jugador 
    pokemon_jug["salud"] -= daño_comp
    print(f"Charmander usó {ataque_comp} y causó {daño_comp:.2f} puntos de daño.")

    if pokemon_jug["salud"] <= 0:
        print("¡La computadora ha ganado la batalla!")