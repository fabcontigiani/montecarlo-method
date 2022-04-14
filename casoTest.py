import random
import time
from carta import Carta
from jugador import Jugador
from envido import envido

ITERACIONES = 10_0
PUNTOS_PARA_GANAR = 15
start_time = time.time()

jugador1 = Jugador()
jugador2 = Jugador()
turno = None

victoriasJ1 = 0
victoriasJ2 = 0
esMano = random.randint(1,2)
if esMano == 1:
    turno = 1
else:
    turno = 2

Partidas = []
Partida = 0

for k in range(ITERACIONES):
    jugador1.puntos = 0
    jugador2.puntos = 0
    Partidas.append(Partida)
    Partida = 0
    while jugador1.puntos < PUNTOS_PARA_GANAR and jugador2.puntos < PUNTOS_PARA_GANAR:
        # Se mezclan las cartas
        mazo = []
        for numero in (1,2,3,4,5,6,7,10,11,12):
            for palo in ("Espada","Basto","Oro","Copa"):
                mazo.append(Carta(numero,palo))

        jugador1.mano = []
        jugador1.tantos = 0
        jugador2.mano = []
        jugador2.tantos = 0
        trucoQuerido = False
        cartasJugadasPorJ1 = []
        cartasJugadasPorJ2 = []
        jugador1.manosGanadas = 0
        jugador2.manosGanadas = 0

        # for j in range(3): # Se reparten 3 cartas
        #     jugador1.mano.append(mazo.pop(random.randint(0, len(mazo)-1)))
        #     jugador2.mano.append(mazo.pop(random.randint(0, len(mazo)-1)))
        if esMano == 1:
            for j in range(3): # Se reparten 3 cartas
                jugador1.mano.append(mazo.pop(random.randint(0, len(mazo)-1)))
                jugador2.mano.append(mazo.pop(random.randint(0, len(mazo)-1)))
        else:
            for j in range(3): # Se reparten 3 cartas
                jugador2.mano.append(mazo.pop(random.randint(0, len(mazo)-1)))
                jugador1.mano.append(mazo.pop(random.randint(0, len(mazo)-1)))
        jugador1.calcular_tanto()
        jugador1.mano.sort()
        jugador2.calcular_tanto()
        jugador2.mano.sort()

        # # Manos de los jugadores
        # print(*jugador1.mano)
        # print(jugador1.tantos)
        # print(*jugador2.mano)
        # print(jugador2.tantos)

        # if esMano == 1: # Jugador 1 es mano
        #     if jugador1.decidirEnvido():
        #         # print(f"Jugador 1: Envido ({jugador1.tantos} tantos)")
        #         envido(jugador1,jugador2)

        if esMano == 1:
            if jugador1.decidirEnvido():
                # print(f"Jugador 1: Envido ({jugador1.tantos} tantos)")
                envido(jugador1,jugador2)
            else:
                if jugador2.decidirEnvido():
                    # print(f"Jugador 2: Envido ({jugador2.tantos} tantos)")
                    envido(jugador2,jugador1)

        else:
            if jugador2.decidirEnvido():
                # print(f"Jugador 2: Envido ({jugador2.tantos} tantos)")
                envido(jugador2,jugador1)
            else:
                if jugador1.decidirEnvido():
                    # print(f"Jugador 1: Envido ({jugador1.tantos} tantos)")
                    envido(jugador1,jugador2)

        for i in range(3):
            if turno == 1:
                if jugador1.decidirTruco(cartasJugadasPorJ2):
                    if jugador2.decidirTruco(cartasJugadasPorJ1):
                        trucoQuerido = True
                    else:
                        jugador1.puntos += 1
                        break
                cartasJugadasPorJ1.append(jugador1.jugarCarta())

                if jugador2.decidirTruco(cartasJugadasPorJ1):
                    if jugador1.decidirTruco(cartasJugadasPorJ2):
                        trucoQuerido = True
                    else:
                        jugador2.puntos += 1
                        break
                cartasJugadasPorJ2.append(jugador2.jugarCarta(cartaRival = cartasJugadasPorJ1[i]))
            else:
                if jugador2.decidirTruco(cartasJugadasPorJ1):
                    if jugador1.decidirTruco(cartasJugadasPorJ2):
                        trucoQuerido = True
                    else:
                        jugador2.puntos += 1
                        break
                cartasJugadasPorJ2.append(jugador2.jugarCarta())

                if jugador1.decidirTruco(cartasJugadasPorJ2):
                    if jugador2.decidirTruco(cartasJugadasPorJ1):
                        trucoQuerido = True
                    else:
                        jugador1.puntos += 1
                        break
                cartasJugadasPorJ1.append(jugador1.jugarCarta(cartaRival=cartasJugadasPorJ2[i]))

            # print(cartasJugadasPorJ1)
            # print(cartasJugadasPorJ2)

            if cartasJugadasPorJ1[i].valorTruco > cartasJugadasPorJ2[i].valorTruco:
                jugador1.manosGanadas += 1
                turno = 1
            elif cartasJugadasPorJ1[i].valorTruco == cartasJugadasPorJ2[i].valorTruco:
                jugador1.manosGanadas += 1
                jugador2.manosGanadas += 1
                turno = esMano
            else:
                jugador2.manosGanadas += 1
                turno = 2


        # Asignacion puntos
        if jugador1.manosGanadas == 2 and jugador1.manosGanadas != jugador2.manosGanadas:
            if trucoQuerido:
                jugador1.puntos += 2
            else:
                jugador1.puntos += 1

        if jugador2.manosGanadas == 2 and jugador1.manosGanadas != jugador2.manosGanadas:
            if trucoQuerido:
                jugador2.puntos += 2
            else:
                jugador2.puntos += 1

        # Situacion triple parda
        if jugador1.manosGanadas == jugador2.manosGanadas == 3:
            if esMano == 1:
                if trucoQuerido:
                    jugador1.puntos += 2
                else:
                    jugador1.puntos += 1
            else:
                if trucoQuerido:
                    jugador2.puntos += 2
                else:
                    jugador2.puntos += 1

        # print(f"Puntos J1: {jugador1.puntos}")
        # print(f"Puntos J2: {jugador2.puntos}")
        Partida +=1
        if esMano == 1:
            esMano = 2
            turno = 2
        else:
            esMano = 1
            turno = 1
        

    if jugador1.puntos >= PUNTOS_PARA_GANAR and jugador1.puntos > jugador2.puntos:
        # print("Victoria Jugador 1")
        victoriasJ1 += 1
    elif jugador2.puntos >= PUNTOS_PARA_GANAR and jugador2.puntos > jugador1.puntos:
        # print("Victoria Jugador 2")
        victoriasJ2 += 1
    else:
        victoriasJ1 += 0.5
        victoriasJ2 += 0.5
    
Q=0
for P in Partidas:
    Q +=P
PartidaMedia = Q/ITERACIONES
print(f"Media de las Partidas: {PartidaMedia}")
print(f"Iteraciones: {ITERACIONES}")
print(f"% victoria Jugador 1: {(victoriasJ1/ITERACIONES)*100:.2f}%")
print(f"% victoria Jugador 2: {(victoriasJ2/ITERACIONES)*100:.2f}%")
print("--- %s seconds ---" % (time.time() - start_time))
