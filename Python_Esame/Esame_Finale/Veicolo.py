###### Marco Pacchiotti 016	######
from abc import ABC, abstractmethod


class Veicolo:
    def __init__(self, marca: str, targa: str, costo: float):
        self.__marca = marca
        self.__targa = targa
        self.__costo = costo

    def get_marca(self):
        return self.__marca

    def __str__(self):
        st = f"marca: {self.__marca:<18} targa: {self.__targa:<18} costo: {self.__costo:<18}"
        return st

    def get_targa(self):
        return self.__targa

    def get_costo(self):
        return self.__costo

    def __eq__(self, other):
        if isinstance(other, Veicolo):
            return (other.get_targa() == self.__targa and other.get_marca() == self.__marca and other.get_costo())
        return False

    def set_targa(self, targa):
        self.__targa = targa

    def set_costo(self, supericie):
        self.__costo = supericie
