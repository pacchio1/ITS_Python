class Atleta:
    def __init__(self, nome, cognome,altezza):
        self.__nome=nome
        self.__cognome=cognome
        self.__alteza=altezza
        self.__squadra=""
        self.__visitamedica=False
    def getNome(self):
        return self.__nome
    def getCognome(self):
        return self.__cognome
    def setAltezza(self, altezza):
        self.__alteza=altezza
    def setSquadra(self, squadra):
        self.__squadra=squadra
    def setVisitamedica(self, visita):
        self.__visitamedica=visita
    def __str__(self) -> str:
        pass
def main():
    altezza=input("altezza:")
    Delpiero=Atleta("alessandro","delpiero",175)
    Totti=Atleta("francesco","totti")
    print(Delpiero.getCognome(),Totti.getNome())



main()
