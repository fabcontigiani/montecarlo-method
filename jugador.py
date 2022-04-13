import random

class Jugador:
    probabilidadEnvido = {
        33 : 0.99,
        32 : 0.95,
        31 : 0.91,
        30 : 0.87,
        29 : 0.83,
        28 : 0.79,
        27 : 0.75,
        26 : 0.71,
        25 : 0.67,
        24 : 0.63,
        23 : 0.59,
        22 : 0.55,
        21 : 0.51,
        20 : 0.47,
        7 : 0.43,
        6 : 0.39,
        5 : 0.35,
        4 : 0.31,
        3 : 0.27,
        2 : 0.23,
        1 : 0.19,
        0 : 0.15,
    }

    probabilidadTruco = {}
    j = 0.
    for i in range(2,28):
        probabilidadTruco[i] = j
        j += 0.04
    probabilidadTruco[28] = 1

    def __init__(self) -> None:
        self.puntos = 0
        self.mano = []
        self.tantos = 0
        self.tantosRival = None
        self.manosGanadas = 0

    def calcular_tanto(self):
        mismoPalo = False
        # flor
        # if self.mano[0].palo == self.mano[1].palo == self.mano[2].palo:
        #     self.tantos = 20
        #     for carta in self.mano:
        #         if carta.numero not in (10,11,12):
        #             self.tantos += carta.numero
        #     return

        # dos del mismo palo
        for carta1 in self.mano:
            for carta2 in self.mano:
                if carta1.palo == carta2.palo and carta1 is not carta2:
                    total = 20
                    mismoPalo = True
                    if carta1.numero not in (10,11,12):
                        total += carta1.numero
                    if carta2.numero not in (10,11,12):
                        total += carta2.numero
                    if total > self.tantos:
                        self.tantos = total

        # ninguna carta del mismo palo
        if not mismoPalo:
            for carta in self.mano:
                if carta.numero > self.tantos and carta.numero not in (10,11,12):
                    self.tantos = carta.numero

    def decidirEnvido(self):
        if random.random() <= self.probabilidadEnvido[self.tantos]:
            return True
        return False

    def decidirTruco(self, cartasJugadasRival):
        if len(self.mano) == 3: # Primera ronda
            if cartasJugadasRival == []: # Rival no ha jugado carta aun
                # Sumamos el valorTruco de las dos cartas mas altas (mano ya ordenado)
                sumaValorTruco = self.mano[-1].valorTruco + self.mano[-2].valorTruco 
            else: # Rival ha jugado 1 carta
                # Chequeamos si alguna de nuestras cartas mata a la del rival
                

                # for carta in self.mano:
                #     if carta.valorTruco > cartasJugadasRival[0].valorTruco:
                #         # Matamos la carta rival, consideramos nuestras 2 cartas de menos valor
                #         sumaValorTruco = self.mano[0].valorTruco + self.mano[1].valorTruco
                #         if random.random() <= self.probabilidadTruco[sumaValorTruco]:
                #             return True
                #         return False
                # # No matamos la carta rival, considaramos nuestras 2 cartas de mayor valor
                # sumaValorTruco = self.mano[-1].valorTruco + self.mano[-2].valorTruco 


                for carta in self.mano:
                    if carta.valorTruco > cartasJugadasRival[0].valorTruco:
                        # Matamos la carta rival, consideramos nuestras 2 cartas de menos valor
                        sumaValorTruco = self.mano[0].valorTruco + self.mano[1].valorTruco
                        break
                else:
                    sumaValorTruco = self.mano[-1].valorTruco + self.mano[-2].valorTruco 


            if random.random() <= self.probabilidadTruco[sumaValorTruco]:
                return True
            return False

        elif len(self.mano) == 2: # Segunda ronda
            if len(cartasJugadasRival) == 1:
                # Ambos jugadores han jugado exactamente 1 carta
                if self.manosGanadas == 1:
                    # Ya hemos ganamos una mano, solo tomamos en cuenta nuestra carta
                    # mas alta, y la multiplicamos por 2
                    sumaValorTruco = self.mano[-1].valorTruco * 2
                else:
                    # El rival ha ganado 1 mano, tomamos en cuenta nuestras 2 cartas
                    # restantes
                    sumaValorTruco = self.mano[0].valorTruco + self.mano[1].valorTruco
                if random.random() <= self.probabilidadTruco[sumaValorTruco]:
                    return True
                return False
            elif len(cartasJugadasRival) == 2:
                # Nosotros hemos jugado 1 carta mientras que el rival ha jugado 2
                if self.manosGanadas == 1:
                    # Hemos ganado la mano anterior, entonces
                    # venciendo la carta rival en la presente mano seriamos vencedores
                    for carta in self.mano:
                        if carta.valorTruco > cartasJugadasRival[-1].valorTruco:
                            # Ganamos
                            return True
                    # Ninguna de nuestras cartas vence la que acaba de jugar el rival, 
                    # tenemos en cuenta nuestra carta mas alta
                    sumaValorTruco = self.mano[-1].valorTruco * 2
                    if random.random() <= self.probabilidadTruco[sumaValorTruco]:
                        return True
                    return False
                else:
                    # El rival ha ganado la mano anterior
                    for carta in self.mano:
                        if carta.valorTruco > cartasJugadasRival[-1].valorTruco:
                            # Una de nuestras cartas mata la que acaba de jugar el rival
                            for carta2 in self.mano:
                                if carta2 is not carta:
                                    # Tomamos en cuenta la otra carta para decidir
                                    sumaValorTruco = carta2.valorTruco * 2
                                    if random.random() <= self.probabilidadTruco[sumaValorTruco]:
                                        return True
                                    return False
                    # Perderemos
                    return False

        elif len(self.mano) == 1:
            if len(cartasJugadasRival) == 2:
                # El rival aun no ha jugado su ultima carta
                sumaValorTruco = self.mano[0].valorTruco * 2
                if random.random() <= self.probabilidadTruco[sumaValorTruco]:
                    return True
                return False
            else:
                # El rival ya ha jugado su ultima carta
                if self.mano[0].valorTruco > cartasJugadasRival[-1].valorTruco:
                    return True
                return False

        else:
            # 0 cartas en mano
            return False

    def jugarCarta(self, cartaRival = None):
        if cartaRival != None:
            cartaQueMata = None
            for carta in self.mano:
                # TODO agregar situacion parda
                if carta.valorTruco > cartaRival.valorTruco:
                    cartaQueMata = carta
                    break

            if cartaQueMata != None:
                self.mano.remove(cartaQueMata)
                # print(cartaQueMata)
                return cartaQueMata
            else:
                menorCarta = self.mano.pop(0)
                # print(menorCarta)
                return menorCarta
        else:
            mayorCarta = self.mano.pop()
            # print(mayorCarta)
            return mayorCarta
