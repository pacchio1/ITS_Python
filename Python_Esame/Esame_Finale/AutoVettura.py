###### Marco Pacchiotti 016	######
from Veicolo import Veicolo


class AutoVettura(Veicolo):

    def __init__(self, marca: str, targa: str, costo: float, posti: int):
        super().__init__(marca, targa, costo)
        self.__posti = posti

    def __str__(self):
        return super().__str__() + f"posti: {self.__posti} "

    def get_posti(self):
        return self.__posti

    def set_posti(self, posti):
        self.__posti = posti

    def __eq__(self, other):
        if isinstance(other, Veicolo):
            return (super().__eq__(other) and other.get_posti() == self.__posti)
