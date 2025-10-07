import random

j1 = 0
j2 = 0
# Opciones a elegir, si no escribe una de estas solicita una nueva opción.
choices = ["piedra", "papel", "tijeras", "lagarto", "spock"]

while j1 < 5 and j2 < 5:
    p1 = input("Elige entre piedra, papel, tijeras, lagarto o spock: ").lower()
    if p1 not in choices:
        print("Opción no válida. Intenta de nuevo.")
        continue

    p2 = random.choice(choices)
    print("La máquina ha sacado:", p2)

    # Comprueba para cada caso si gana o pierde el jugador 1. Si gana se le suma un punto y sino se le suma a la maquina.
    match (p1, p2):
        case (p1, p2) if p1 == p2:
            print("Empate")
        case ("tijeras", "papel") | ("tijeras", "lagarto"):
            print("Jugador 1 gana esta ronda")
            j1 += 1
        case ("papel", "piedra") | ("papel", "spock"):
            print("Jugador 1 gana esta ronda")
            j1 += 1
        case ("piedra", "lagarto") | ("piedra", "tijeras"):
            print("Jugador 1 gana esta ronda")
            j1 += 1
        case ("lagarto", "spock") | ("lagarto", "papel"):
            print("Jugador 1 gana esta ronda")
            j1 += 1
        case ("spock", "tijeras") | ("spock", "piedra"):
            print("Jugador 1 gana esta ronda")
            j1 += 1
        case _:
            print("Jugador 2 gana esta ronda")
            j2 += 1
    print(f"Puntuaciones -> Jugador 1: {j1} | Jugador 2: {j2}")

# Cuando uno de los 2 llegue a 5, sale del bucle e imprime el resultado.
if j1 == 5:
    print("Has ganado la partida")
else:
    print("La máquina gana la partida")