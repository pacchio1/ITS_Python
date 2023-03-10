import os
import ClassImmobili
menu = """
opzione azzione

1)      Crea immobile
2)      Compara immobili
3)      Stampa elenco immobili e il costo
4)      Stampa Calcola costo di un immobile
5)      Stampa immobili in ordine di superficie
6)      Stampa immobili in ordine di numero di stanze
7)      Stampa immobili in ordine di città

0)      ESCI
"""
villa1 = ClassImmobili.Villa(
    6, 200, "via le mani dal naso", "Napoli", 2002, True, 2, True)
villa2 = ClassImmobili.Villa(
    5, 220, "via dalle palle", "Cuneo", 2005, False, 1, False)
villa1clone = ClassImmobili.Villa(
    6, 200, "via le mani dal naso", "Napoli", 2002, True, 2, True)

abitazione1 = ClassImmobili.Abitazione(
    3, 100, "Via Roma 1", "Roma", 1950, True)
villa1 = ClassImmobili.Villa(
    6, 200, "Via dei Giardini 2", "Milano", 1980, True, 2, True)
appartamento1 = ClassImmobili.Appartamento(
    2, 50, "Corso Italia 10", "Torino", 2000, 3)

scelta = -1
gestione_mobili = ClassImmobili.GestioneImmobili()
gestione_mobili.aggiungi_immobile(villa1)
gestione_mobili.aggiungi_immobile(villa1clone)
gestione_mobili.aggiungi_immobile(villa2)
gestione_mobili.aggiungi_immobile(abitazione1)
gestione_mobili.aggiungi_immobile(villa1)
gestione_mobili.aggiungi_immobile(appartamento1)


def CreaImmobile():
    print(
        "che tipo di immobile si vuole creare:  1Abitazione  ///   2Villa  ///   3Appartamento")
    while True:
        try:
            n = int(input(":"))
            if n == 1:
                ns = int(input("n stanze:"))
                s = float(input("superficie:"))
                i = input("indirizo:")
                c = input("citta:")
                ac = int(input("anno costruzione:"))
                co = bool(input("cortile:"))
                return ClassImmobili.Abitazione(ns, s, i, c, ac, co)

            elif n == 2:
                ns = int(input("n stanze:"))
                s = float(input("superficie:"))
                i = input("indirizo:")
                c = input("citta:")
                ac = int(input("anno costruzione:"))
                g = input("giardino True/False:")
                np = int(input("n piani:"))
                pi = bool(input("piscina:"))
                return ClassImmobili.Villa(ns, s, i, c, ac, g, np, pi)

            elif n == 3:
                ns = int(input("n stanze:"))
                s = float(input("superficie:"))
                i = input("indirizo:")
                c = input("citta:")
                ac = int(input("anno costruzione:"))
                np = int(input("n piano:"))
                return ClassImmobili.Appartamento(ns, s, i, c, ac, np)

        except:
            print("errore")
            print(menu)


def comparaImmobili(gestione_mobili):
    gestione_mobili.elencoImmobili()
    while True:
        try:
            a = input("immobile 1:")
            b = input("immobile 2:")
            break
        except:
            print("errore")
            imm1 = gestione_mobili.cercaImmobile(int(a))
            imm2 = gestione_mobili.cercaImmobile(int(b))
            if imm1 == imm2:
                print("gli imobili sono uguali")
            else:
                print("gli imobili non sono uguali")


while scelta != 0:
    os.system("cls")
    print(menu)
    scelta = (input(':'))
    match scelta:
        case '1':
            print("operazione", scelta)
            CreaImmobile()
        case '2':
            print("operazione", scelta)
            print(
                "Compara due immobili")
            comparaImmobili(gestione_mobili)

        case '3':
            print("operazione", scelta)
            elenco = gestione_mobili.elencoImmobili()
            print(elenco)
        case '4':
            print("operazione", scelta)
            gestione_mobili.elencoImmobili()
            while True:
                try:
                    a = input("immobile 1:")
                    b = input("immobile 2:")
                    break
                except:
                    print("errore")
                    imm1 = gestione_mobili.cercaImmobile(int(a))

        case '5':
            print("operazione", scelta)

        case '6':
            print("operazione", scelta)

        case '7':
            print("operazione", scelta)

        case '0':
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
