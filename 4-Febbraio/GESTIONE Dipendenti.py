class Dipendente(object):
    def __init__(self, nome, cognome, indirizo, sesso):
        self._nome = nome  # attributo protetto
        self._cognome = cognome  # attributo protetto
        self.__indirizo = indirizo
        self.__sesso = sesso

    def __str__(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome+" Indirizo", self.__indirizo, "sesso", self.__sesso

    def GetIndirizo(self):
        return self.__indirizo

    def GetNome(self):
        return "Nome: "+self._nome+" Cognome: "+self._cognome

    def GetSesso(self):
        return self.__sesso

    def SetIndirizo(self, input):
        self.__indirizo = input

    def SetNome(self, nome, cognome):
        self.__nome = nome
        self.__cognome = cognome

    def SetSesso(self, sex):
        self.__sesso = sex


class Impiegato(Dipendente):
    def __init__(self, nome, cognome, indirizo, sesso, ufficio):
        Dipendente().__init__(nome, cognome, indirizo, sesso)
        self.__ufficio = ufficio

    def get_Ufficio(self):
        return self.__ufficio

    def set_Ufficio(self, eta):
        self.__ufficio = eta

    def __str__(self):
        None


class docente(Dipendente):
    def __init__(self, nome, cognome, indirizo, sesso, disciplina, ruolo):
        Dipendente().__init__(nome, cognome, indirizo, sesso)
        self.__disciplina = disciplina
        self.__ruolo = ruolo

    def get_disciplina(self):
        return self.__disciplina

    def set_disciplina(self, eta):
        self.__disciplina = eta

    def get_ruolo(self):
        return self.__ruolo

    def set_ruolo(self, eta):
        self.__ruolo = eta

    def __str__(self):
        None


class GestioneDipendenti(Dipendente):
    def __init__(self, nome, cognome, indirizo, sesso):
        Dipendente().__init__(nome, cognome, indirizo, sesso)
        self.__elenco = []

    def get_elenco(self):
        return self.__elenco

    def set_elenco(self, eta):
        self.__elenco = eta

    def __str__(self):
        None

    def aggiungidipendente(nome, cognome, indirizo, sesso):
        Dipendente.__init__(nome, cognome, indirizo, sesso)

    def eliminadipendente(nome):
        Dipendente.remove(nome)

    def cercadipendente(nome):
        Dipendente.find(nome)

    def cancella_tutti_dip():
        Dipendente.clear()

    def totale_dipendenti():
        Dipendente.count()

    def stampa_dipendenti():
        for i in Dipendente:
            print(Dipendente[i].__str__)
