import random

class Jugador:
    probabilidadEnvido =  {
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

    def __init__(self) -> None:
        self.puntos = 0
        self.mano = []
        self.tantos = 0
        self.tantosRival = None

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
        # if self.tantos >= 27:
        #     return True
        # return False
        if random.random() >= self.probabilidadEnvido[self.tantos]:
            return True
        return False
