###### Marco Pacchiotti 016	######
class GestioneVeicoli:
    def __init__(self):
        self.__elenco = []

    def aggiungi_veicolo(self, veicolo):
        self.__elenco.append(veicolo)

    def cerca_veicolo(self, targa):
        for i, veicolo in enumerate(self.__elenco):
            if veicolo.get_targa() == targa:
                print("in posizione", i+1, veicolo)

    def cancella_veicolo(self, targa):
        flag = 0
        for veicolo in self.__elenco:
            if veicolo.get_targa() == targa:
                self.__elenco.remove(veicolo)
                flag = 1
        if flag == 0:
            print("veicolo non trovato")

    def totale_veicoli(self) -> str:
        i = 0
        for veicolo in self.__elenco:
            i = i+1
        print("Totale Veicoli", i)

    def stampa_veicoli(self):
        for i, ve in enumerate(self.__elenco):
            print(f"{i+1}   {ve}")

    def costo_totale(self) -> float:
        costo = 0.0
        for ve in self.__elenco:
            costo = costo + float(ve.get_costo())
        print("il costo totale delle auto e di:", costo)

    def ordina_veicoli(self):
        self.__elenco.sort(key=lambda immobile: immobile.get_targa())
