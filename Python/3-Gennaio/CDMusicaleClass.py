class CD:
    def __init__(self,titolo,durata,anno,tracce):
        self.__titolo=titolo
        self.__durata=durata
        self.__anno=anno
        self.__tracce=tracce
    def getTitolo(self):
        return self.__titolo
    def getDurata(self):
        return self.__durata
    def getAnno(self):
        return self.__anno
    def getTrak(self):
        return self.__tracce
    def setAltezza(self, altezza):
        self.__alteza=altezza
