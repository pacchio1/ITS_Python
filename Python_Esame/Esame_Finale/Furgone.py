###### Marco Pacchiotti 016	######
from Veicolo import Veicolo


class Furgone(Veicolo):

    def __init__(self, marca: str, targa: str, costo: float, capacita: int):
        super().__init__(marca, targa, costo)
        self.__capacita = capacita

    def __str__(self):
        return super().__str__() + f"capacita: {self.__capacita} "

    def get_capacita(self):
        return self.__capacita

    def set_capacita(self, capacita):
        self.__capacita = capacita

    def __eq__(self, other):
        if isinstance(other, Veicolo):
            return (super().__eq__(other) and other.get_capacita() == self.__capacita)
