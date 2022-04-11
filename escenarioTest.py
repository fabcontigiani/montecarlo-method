import random
from carta import Carta
from jugador import Jugador
from envido import envido

ITERACIONES = 1
PUNTOS_PARA_GANAR = 15

jugador1 = Jugador()
jugador2 = Jugador()

# Primer Turno
siguienteMano = random.randint(0,1)

for i in range(ITERACIONES):
    jugador1.puntos = 0
    jugador2.puntos = 0

    while jugador1.puntos < PUNTOS_PARA_GANAR and jugador2.puntos < PUNTOS_PARA_GANAR:
        # Se mezclan las cartas
        mazo = []
        for numero in (1,2,3,4,5,6,7,10,11,12):
            for palo in ("Espada","Basto","Oro","Copa"):
                mazo.append(Carta(numero,palo))

        # Se reparte
        jugador1.mano = []
        jugador1.tantos = 0
        jugador2.mano = []
        jugador2.tantos = 0
        for i in range(3):
            jugador1.mano.append(mazo.pop(random.randint(0,len(mazo)-1)))
            jugador2.mano.append(mazo.pop(random.randint(0,len(mazo)-1)))
        jugador1.calcular_tanto()
        jugador2.calcular_tanto()

        # # Manos de los jugadores
        # print(*jugador1.mano)
        # print(jugador1.tantos)
        # print(*jugador2.mano)
        # print(jugador2.tantos)

        if siguienteMano == 0:
            # juega jugador 1
            siguienteMano = 1
            if jugador1.decidirEnvido():
                print(f"Jugador 1: Envido ({jugador1.tantos} tantos)")
                envido(jugador1,jugador2)
            
            

        else:
            # juega jugador 2
            siguienteMano = 0
            if jugador2.decidirEnvido():
                print(f"Jugador 2: Envido ({jugador2.tantos} tantos)")
                envido(jugador2,jugador1)

    if jugador1.puntos >= PUNTOS_PARA_GANAR:
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")