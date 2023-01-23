class CD:
    def __init__(self,titolo,durata,anno,tracce,prezzo):
        self.__titolo=titolo
        self.__durata=durata
        self.__anno=anno
        self.__tracce=tracce
        self.__prezzo=prezzo
    def getTitolo(self):
        return self.__titolo
    def getDurata(self):
        return self.__durata
    def getAnno(self):
        return self.__anno
    def getTrak(self):
        return self.__tracce
    def getPrice(self):
        return self.__prezzo
    def setPrezzo(self, prezzo):
        self.__prezzo=prezzo
