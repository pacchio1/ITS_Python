class Persona:
    def __init__(self, nome, cognome) -> None:
        self.__nome = nome
        self.__cognome = cognome
        self.__conto = None

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def getConto(self):
        return self.__conto

    def setNome(self, nome):
        self.__nome = nome

    def setCognome(self, cognome):
        self.__cognome = cognome

    def setConto(self, conto):
        self.__conto = conto

    def __str__(self) -> str:
        return f" nome :{self.__nome}, cognome: {self.__cognome}"
