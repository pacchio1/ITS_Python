###### Marco Pacchiotti 016	######
# menu
import os
from datetime import date
spesa = []
articolo = []
sconto_a = 0
totale = 0
flag = False
oggi = date.today()
conto = "{:<20}{:<8}{:<8}{:<8}{:<8}"


def sconto(n, perc):
    return n-(n*(perc/100))

# def indati():


def stampaNS():
    i = 0
    print(oggi)
    print("ARTICOLO     PREZZO      QUANTITA’       TOTALE")

    while i < len(spesa):
        #print((spesa[i][0])+" "+(spesa[i][0])+" "+(spesa[i][0])+(spesa[i][0]))
        tmp = (spesa[i])
        articolo=(tmp[0])
        prezzo=(tmp[1])
        quantita=(tmp[2])
        ToT=(tmp[3])

        txt = "{:.<13} {:<12} {:<12} {:<12}"
        print(txt.format(articolo,prezzo,quantita,ToT))
        i = i+1


def stampaSS():
    i = 0
    print(oggi)
    print("ARTICOLO     PREZZO      QUANTITA’       TOTALE SCONTATO        SCONTO APPLICATO  ")

    while i < len(spesa):
        aux = sconti_muti(i)
        tmp = (spesa[i])
        articolo=(tmp[0])
        prezzo=(tmp[1])
        quantita=(tmp[2])
        ToT=(tmp[3])
        sconto_a=(aux)
        sconto_a=ToT-sconto_a
        txt = "{:<13} {:<13} {:<13} {:<13} {:<13}"
        print(txt.format(articolo,prezzo,quantita,ToT,sconto_a))
        i = i+1

def sconti_muti(i):

    totale = spesa[i][1]*spesa[i][2]
    if totale >= 50.0 and spesa[i][2] > 5:

        totale = sconto(totale, 10)

        totale = sconto(totale, 5)

    elif totale >= 50.0:

        totale = sconto(totale, 10)

    elif spesa[i][2] > 5:

        totale = sconto(totale, 5)
    else:
        None
    return totale
def sconti(i):

    totale = spesa[i][1]*spesa[i][2]
    if totale >= 50.0 and spesa[i][2] > 5:
        print("sconto del 10% per totale >= 50 €", totale)
        totale = sconto(totale, 10)
        print("sconto del 5% per 5 o piu articoli uguale/i", totale)
        totale = sconto(totale, 5)
        print("per un totale di", totale)
    elif totale >= 50.0:
        print("sconto del 10% per totale >= 50 €", totale)
        totale = sconto(totale, 10)
        print("per un totale di", totale)
    elif spesa[i][2] > 5:
        print("sconto del 5% per 5 o piu articoli uguale/i", totale)
        totale = sconto(totale, 5)
    else:
        print(totale)
    return totale


def riordina_i():
    while True:
        tmp = input(
            "stampa ordinata in base prezzo [b] stampa ordinata in base alla quantità [q]")
        if tmp == 'b':
            tmp = 2
            break
        elif tmp == 'q':
            tmp = 1
            break
        else:
            print("errore input")
    spesa.sort(key=lambda x: x[tmp])
    return spesa


def articoli():
    i = 0
    while i < len(spesa):
        tmp = spesa[i]

        print(tmp[0]+" "+(str(tmp[2])))
        i = i+1


Menu = """
---------------------------------------------------------
        1) Inserimento articolo
        2) Totale Articoli venduti
        3) Totale degli sconti effettuati
        4) Stampa scontrino senza sconto
        5) Stampa scontrino con lo sconto
        6) Stampa scontrino con sconto ordinato per prezzo o per quantità a scelta
        0) Fine
---------------------------------------------------------
"""
scelta = -1
while scelta != 0:
    os.system("cls")
    print(Menu)
    scelta = input(':')
    match scelta:
        case '1':
            print("operazione", scelta)
            articolo = []
            nome = input("Nome prodotto:")
            while True:
                try:

                    prezzo = float(input("Prezzo:"))
                    quantita = int(input("Quantita:"))
                    totale = prezzo*quantita
                    articolo.append(nome)
                    articolo.append(prezzo)
                    articolo.append(quantita)
                    articolo.append(totale)
                    spesa.append(articolo)
                    break
                except:
                    print("errore")
                    break

        case '2':
            print("operazione", scelta)
            articoli()

        case '3':
            print("operazione", scelta)
            for i in range(0, len(spesa)):
                sconti(i)

        case '4':
            print("operazione", scelta)
            stampaNS()
        case '5':
            print("operazione", scelta)
            stampaSS()
        case '6':
            print("operazione", scelta)
            riordina_i()
            stampaSS()
        case '0':
            break

        case _:
            print("input sbagliato")

    input("premi invio per continuare")
