valoresTruco = {
    "1 de Espada" : 14,
    "1 de Basto" : 13,
    "7 de Espada" : 12,
    "7 de Oro" : 11,
    "3 de Espada" : 10,
    "3 de Basto" : 10, 
    "3 de Oro" : 10, 
    "3 de Copa" : 10,
    "2 de Espada" : 9, 
    "2 de Basto" : 9, 
    "2 de Oro" : 9, 
    "2 de Copa" : 9,
    "1 de Copa" : 8, 
    "1 de Oro" : 8,
    "12 de Espada" : 7, 
    "12 de Basto" : 7, 
    "12 de Oro" : 7, 
    "12 de Copa" : 7,
    "11 de Espada" : 6, 
    "11 de Basto" : 6, 
    "11 de Oro" : 6, 
    "11 de Copa" : 6,
    "10 de Espada" : 5, 
    "10 de Basto" : 5, 
    "10 de Oro" : 5, 
    "10 de Copa" : 5,
    "7 de Basto" : 4, 
    "7 de Copa" : 4,
    "6 de Espada" : 3, 
    "6 de Basto" : 3, 
    "6 de Oro" : 3, 
    "6 de Copa" : 3,
    "5 de Espada" : 2, 
    "5 de Basto" : 2, 
    "5 de Oro" : 2, 
    "5 de Copa" : 2,
    "4 de Espada" : 1, 
    "4 de Basto" : 1, 
    "4 de Oro" : 1, 
    "4 de Copa" : 1,
}

class Carta:
    def __init__(self, numero: int, palo: str) -> None:
        self.numero = numero
        self.palo = palo
        self.valorTruco = valoresTruco[self.__str__()]

    def mata(self, carta1):
        if self.valorTruco > carta1.valorTruco:
            return True
        return False

    def parda(self, carta1):
        if self.valorTruco == carta1.valorTruco:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.numero} de {self.palo}"

# test1 = Carta(3,"Copa")
# test2 = Carta(7,"Oro")
# test3 = Carta(3,"Copa")
# print(test1.valorTruco)
# print(test2.valorTruco)
# print(test1.mata(test2))
# print(test2.mata(test1))
# print(test1.parda(test3))