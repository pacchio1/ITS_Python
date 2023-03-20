from abc import ABC, abstractmethod


class oggetto:
    def __init__(self, nome: str, stanze: int, superficie: float, indirizzo: str, città: str, anno_costruzione: int, valore_mq: float):
        self.__nome = nome
        self.__stanze = stanze
        self.__superficie = superficie
        self.__indirizzo = indirizzo
        self.__città = città
        self.__anno_costruzione = anno_costruzione
        self.__valore_mq = valore_mq

    def get_nome(self):
        return self.__nome

    def __str__(self):
        st = f"Nome: {self.__nome} Stanze: {self.__stanze:<18} Superficie: {self.__superficie:<18} Indirizzo: {self.__indirizzo:<18} Città: {self.__città} Anno costruzione: {self.__anno_costruzione:<18} Valore mq: {self.__valore_mq:<18} "
        return st

    def __eq__(self, other):
        if isinstance(other, oggetto):
            return (other.get_stanze() == self.__stanze and other.get_superficie() == self.__superficie and
                    other.get_indirizzo() == self.__indirizzo and other.get_città() == self.__città and
                    other.get_anno_costruzione() == self.__anno_costruzione and other.get_valore_mq() == self.__valore_mq)
        return False

    def get_stanze(self):
        return self.__stanze

    def get_superficie(self):
        return self.__superficie

    def get_indirizzo(self):
        return self.__indirizzo

    def get_città(self):
        return self.__città

    def get_anno_costruzione(self):
        return self.__anno_costruzione

    def get_valore_mq(self):
        return self.__valore_mq

    def set_stanze(self, stanze):
        self.__stanze = stanze

    def set_superficie(self, supericie):
        self.__superficie = supericie

    def set_indirizzo(self, indirizzo):
        self.__indirizzo = indirizzo

    def set_città(self, città):
        self.__città = città

    def set_anno_costruzione(self, anno_costruzione):
        self.__anno_costruzione = anno_costruzione

    def set_valore_mq(self, valore_mq):
        self.__valore_mq = valore_mq

    @abstractmethod
    def calcola_valore(self, metro_quadro):
        pass
