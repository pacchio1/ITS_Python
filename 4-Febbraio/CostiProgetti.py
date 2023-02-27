from abc import abstractmethod
from datetime import datetime
anno = datetime.today().year


class Persona(object):
    def __init__(self, nome, cognome, matricola, annoassunzione):
        self._nome = nome  # attributo protetto
        self._cognome = cognome  # attributo protetto
        self.__matricola = matricola
        self.__annoassunzione = annoassunzione

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" matricola", self.__matricola, "annoassunzione", self.__annoassunzione

    def Getmatricola(self) -> str:
        return self.__matricola

    def GetNome(self) -> str:
        return self._nome

    def GetCognome(self) -> str:
        return self.__cognome

    def Getannoassunzione(self) -> int:
        return self.__annoassunzione

    def Setmatricola(self, input):
        self.__matricola = input

    def SetNome(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

    def Setannoassunzione(self, sex):
        self.__annoassunzione = sex

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Persona):
            return (Persona.GetNome() == self.__nome and Persona.GetCognome() == self.__cognome and Persona.Getannoassunzione() == self.__annoassunzione)

    @abstractmethod
    def getcostoC(anno):
        pass


class GestioneProgetti(Persona):

    def __init__(self, nome, cognome, matricola, annoassunzione):
        super().__init__(nome, cognome, matricola, annoassunzione)
        self.__elenco = []

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" matricola", self.__matricola, "annoassunzione", self.__annoassunzione

    def aggiungiPersona(p):
        Persona().__init__

    def eliminaPersona(nome):
        for i in Persona:
            if nome in Persona[i]:
                Persona.remove(i)

    def cercaPersona(nome):
        Persona.find(nome)

    def elencoPersone():
        for individo in Persona:
            Persona[individo].__str__

    def getTotalePersone():
        Persona.count()

    def costiProgetto(self, anno):
        for i in self.__elenco:
            tot = tot+i.getcostoC(anno)
        return tot

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Persona):
            return (GestioneProgetti.elencoPersone() == self.__elencoPersone() and GestioneProgetti.costiProgetto() == self.__costiProgetto())


class TecnicoEleAut(Persona):

    def __init__(self, nome, cognome, matricola, annoassunzione, orelavorate, interno):
        super().__init__(nome, cognome, matricola, annoassunzione)
        self.costo = 50
        self.__orelavorate = orelavorate
        self.__interno = interno

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" matricola", self.__matricola, "annoassunzione", self.__annoassunzion

    def get_orelavorate(self):
        return self.__orelavorate

    def getinterno(self):
        return self.__interno

    def set_orelavorate(self, orelavorate):
        self.orelavorate = orelavorate

    def setinterno(self, interno):
        self.__interno = interno

    def getcostoC(self, anno):
        if TecnicoEleAut.getinterno() == True:
            return TecnicoEleAut.costo + (anno-TecnicoEleAut.Getannoassunzione()) * TecnicoEleAut.get_orelavorate()
        else:
            return TecnicoEleAut.costo * TecnicoEleAut.get_orelavorate()

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Persona):
            return (Persona.GetNome() == self.__nome and Persona.GetCognome() == self.__cognome and Persona.Getannoassunzione() == self.__annoassunzione)


class TecnicoInfTe(Persona):

    def __init__(self, nome, cognome, matricola, annoassunzione, orelavorate, interno):
        super().__init__(nome, cognome, matricola, annoassunzione)
        self.costo = 40
        self.__orelavorate = orelavorate
        self.__interno = interno

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" matricola", self.__matricola, "annoassunzione", self.__annoassunzion

    def get_orelavorate(self):
        return self.__orelavorate

    def getinterno(self):
        return self.__interno

    def set_orelavorate(self, orelavorate):
        self.orelavorate = orelavorate

    def setinterno(self, interno):
        self.__interno = interno

    def getcostoC(self, anno):
        if TecnicoInfTe.getinterno() == True:
            return TecnicoInfTe.costo + (anno-TecnicoInfTe.Getannoassunzione()) * TecnicoInfTe.get_orelavorate()
        else:
            return TecnicoInfTe.costo * TecnicoInfTe.get_orelavorate()

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Persona):
            return (Persona.GetNome() == self.__nome and Persona.GetCognome() == self.__cognome and Persona.Getannoassunzione() == self.__annoassunzione)


class FunzionarioSenior(Persona):

    def __init__(self, nome, cognome, matricola, annoassunzione, orelavorate, interno):
        super().__init__(nome, cognome, matricola, annoassunzione)
        self.costo = 80
        self.__orelavorate = orelavorate
        self.__interno = interno

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" matricola", self.__matricola, "annoassunzione", self.__annoassunzion

    def get_orelavorate(self):
        return self.__orelavorate

    def set_orelavorate(self, orelavorate):
        self.orelavorate = orelavorate

    def getcostoC(self, anno):
        return FunzionarioSenior.costo + (anno-FunzionarioSenior.Getannoassunzione()) * FunzionarioSenior.get_orelavorate()

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Persona):
            return (Persona.GetNome() == self.__nome and Persona.GetCognome() == self.__cognome and Persona.Getannoassunzione() == self.__annoassunzione)


class FunzionarioJunior(Persona):

    def __init__(self, nome, cognome, matricola, annoassunzione, orelavorate, interno):
        super().__init__(nome, cognome, matricola, annoassunzione)
        self.costo = 70
        self.__orelavorate = orelavorate
        self.__interno = interno

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" matricola", self.__matricola, "annoassunzione", self.__annoassunzion

    def get_orelavorate(self):
        return self.__orelavorate

    def set_orelavorate(self, orelavorate):
        self.orelavorate = orelavorate

    def getcostoC(self, anno):
        return FunzionarioJunior.costo + (anno-FunzionarioJunior.Getannoassunzione()) * FunzionarioJunior.get_orelavorate()

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Persona):
            return (Persona.GetNome() == self.__nome and Persona.GetCognome() == self.__cognome and Persona.Getannoassunzione() == self.__annoassunzione)


class Dirigente(Persona):

    def __init__(self, nome, cognome, matricola, annoassunzione, orelavorate, interno):
        super().__init__(nome, cognome, matricola, annoassunzione)
        self.costo = 100
        self.__orelavorate = orelavorate
        self.__interno = interno

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" matricola", self.__matricola, "annoassunzione", self.__annoassunzion

    def get_orelavorate(self):
        return self.__orelavorate

    def set_orelavorate(self, orelavorate):
        self.orelavorate = orelavorate

    def getcostoC(self, anno):
        return Dirigente.costo + (anno-Dirigente.Getannoassunzione()) * Dirigente.get_orelavorate()

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Persona):
            return (Persona.GetNome() == self.__nome and Persona.GetCognome() == self.__cognome and Persona.Getannoassunzione() == self.__annoassunzione)
