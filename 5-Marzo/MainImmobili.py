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
scelta = -1
gestione_mobili = ClassImmobili.GestioneImmobili()
gestione_mobili.aggiungi_immobile((villa1, villa2, villa1clone))


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
            if villa1 == villa1clone:
                print("eq funziona")
            if villa1 != villa2:
                print("eq funziona")
            else:
                print("eq non funziona")

        case '3':
            print("operazione", scelta)
            elenco = gestione_mobili.elencoImmobili()
            print(elenco)
        case '4':
            print("operazione", scelta)
            print(villa1.GetValoreImmobile())
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
