from abc import ABC, abstractmethod


class Immobile(ABC):
    def __init__(self, numero_stanze, superficie, indirizzo, citta, anno_costruzione):
        self.__numero_stanze = numero_stanze  # attributo protetto
        self.__superficie = superficie  # attributo protetto
        self.__indirizzo = indirizzo
        self.__citta = citta
        self.__anno_costruzione = anno_costruzione

    """numero_stanze, superficie, indirizzo e la città, anno_costruzione."""

    def __str__(self):
        st = f"numero_stanze: {self.__numero_stanze} superficie: {self.__superficie} indirizzo, {self.__indirizzo} anno_costruzione {str(self.__anno_costruzione)},città:, {self.__citta}"
        return st

    def GetIndirizzo(self) -> str:
        return self.__indirizzo

    def GetNStanze(self) -> int:
        return self.__numero_stanze

    def GetSuperficie(self) -> float:
        return self.__superficie

    def GetCitta(self) -> str:
        return self.__citta

    def GetAnnoCostruzione(self) -> int:
        return self.__anno_costruzione

    def SetIndirizzo(self, indirizzo):
        self.__indirizzo = indirizzo

    def SetNStanze(self, numero_stanze):
        self.__numero_stanze = numero_stanze

    def SetSupSuperficie(self, superficie):
        self.__superficie = superficie

    def SetAnnoCostruzione(self, anno_costruzione):
        self.__anno_costruzione = anno_costruzione

    def __eq__(self, o) -> bool:
        if isinstance:
            return (self.GetIndirizzo() == o.GetIndirizzo() and self.GetCitta() == o.GetCitta())

    @abstractmethod
    def GetValoreImmobile():
        pass


class Abitazione(Immobile):
    val = 2500

    def __init__(self, numero_stanze, superficie, indirizzo, citta, anno_costruzione, cortile):
        super().__init__(numero_stanze, superficie, indirizzo, citta, anno_costruzione)
        self.__cortile = cortile
        if anno_costruzione <= 1940:
            Abitazione.val = 2500-(2500*0.2)

    def __str__(self):
        return super().__str__()

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def GetCortile(self) -> bool:
        return self.__anno_costruzione

    def SetCortile(self, cortile):
        self.__cortile = cortile

    def GetValore(self):
        return Abitazione.val

    def GetValoreImmobile(self):
        s = self.GetSuperficie()
        v = self.GetValore()
        return s*v


class Villa(Immobile):
    val = 3500

    def __init__(self, numero_stanze, superficie, indirizzo, citta, anno_costruzione, giardino, n_piani, piscina):
        super().__init__(numero_stanze, superficie, indirizzo, citta, anno_costruzione)
        self.__giardino = giardino
        self.__n_piani = n_piani
        self.__Piscina = piscina
        if anno_costruzione <= 1940:
            Villa.val = 2500-(2500*0.25)

    def __str__(self):
        return super().__str__()

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def Getgiardino(self) -> float:
        return self.__anno_costruzione

    def SetPiani(self, giardino):
        self.__indirizzo = giardino

    def GetPiani(self) -> int:
        return self.__anno_costruzione

    def Setgiardino(self, n_piani):
        self.__n_piani = n_piani

    def GetPiscina(self) -> bool:
        return self.__piscina

    def SetPiscina(self, piscina):
        self.__piscina = piscina

    def GetValore(self):
        return Villa.val

    def GetValoreImmobile(self):
        s = self.GetSuperficie()
        v = self.GetValore()
        return s*v


"""villa1clone = Villa(
    6, 200, "via le mani dal naso", "Napoli", 2002, True, 2, True)
print(villa1clone)"""


class Appartamento(Immobile):
    val = 1750

    def __init__(self, numero_stanze, superficie, indirizzo, citta, anno_costruzione, n_piano):
        super().__init__(numero_stanze, superficie, indirizzo, citta, anno_costruzione)
        self.__n_piano = n_piano
        if anno_costruzione <= 1940:
            Appartamento.val = 2500-(2500*0.15)

    def GetNPiano(self) -> float:
        return self.__n_piano

    def SetNPiano(self, n_piano):
        self.__indirizzo = n_piano

    def __str__(self):
        return super().__str__() + str(self.__n_piano)

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o) and self.GetNPiano() == __o.GetNPiano()

    def GetValore(self):
        return Appartamento.val

    def GetValoreImmobile(self):
        s = self.GetSuperficie()
        v = self.GetValore()
        return s*v


class GestioneImmobili(object):

    def __init__(self):
        self.__elenco = []

    def __str__(self):
        super().__str__()

    def aggiungi_immobile(self, immobile):
        self.__elenco.append(immobile)

    def elencoImmobili(self) -> str:
        for i, im in enumerate(self.__elenco):
            print(f"{i+1}   {im}")

    def cercaImmobile(self, num):
        return self.__elenco[num-1]
    def valoreImmobile(self, immobile_in):
        for im in self.__elenco:
            if im==immobile_in:
                return isinstance(im)
        
