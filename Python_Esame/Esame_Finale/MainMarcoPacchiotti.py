###### Marco Pacchiotti 016	######
from AutoVettura import AutoVettura
from Furgone import Furgone
from Veicolo import Veicolo
from GestioneVeicoli import GestioneVeicoli
import os


def int_input(testo):
    while True:
        try:
            n = int(input(testo))
            return n
        except:
            print("errore")


DefaultVeicolo = Veicolo('fiat', 'ff567aa', 8000)
DefaultFurgone = Furgone('fiat', 'dd965aa', 11000, 50)
DefaultAutoVettura = AutoVettura("audi", "er999li", 15000, 5)
GV = GestioneVeicoli()
GV.aggiungi_veicolo(DefaultVeicolo)
GV.aggiungi_veicolo(DefaultFurgone)
GV.aggiungi_veicolo(DefaultAutoVettura)
Menu = """
----------------------------------------------------------------------------
|    1) permette di prendere input i dati di un veicolo                     |
|    2) permette la cancellazione di un veicolo ricercato per Targa         |
|    3) stampa la posizione di un veicolo nell’elenco cercato per targa     |
|    4) stampa dell’elenco dei veicoli in ordine di targa                   |
|    5) stampa il numero totale dei veicoli                                 |
|    6) stampa il costo totale dei veicoli                                  |

     0) fine
----------------------------------------------------------------------------
"""


def punto1(m, t, c, sce, o):
    if sce == '0':
        Veicolox = Veicolo(m, t, c)
        GV.aggiungi_veicolo(Veicolox)
    elif sce == "1":
        Veicolox = AutoVettura(m, t, c, o)
        GV.aggiungi_veicolo(Veicolox)
    elif sce == "2":
        Veicolox = Furgone(m, t, c, o)
        GV.aggiungi_veicolo(Veicolox)


def punto2(GV, targa):
    GV.cancella_veicolo(targa)


def punto3(GV, targa):
    GV.cerca_veicolo(targa)


def punto4(GV):
    GV.ordina_veicoli()
    GV.stampa_veicoli()


def punto5(GV):
    GV.totale_veicoli()


def punto6(GV):
    GV.costo_totale()


scelta = -1
while scelta != 0:
    os.system("cls")
    print(Menu)
    scelta = (input(':'))
    match scelta:
        case '1':
            o = 0
            print("operazione", scelta)
            m = input("marca:")
            t = input("targa:")
            c = int_input("costo:")
            sce = '-1'
            sce = input(
                "scegliere 0 per Veicolo 1 Per Auto vettura 2 per furgone:")
            if sce == '1':
                o = int_input("posti:")
            if sce == '2':
                o = int_input("Litri Quadrati:")
            punto1(m, t, c, sce, o)

        case '2':
            print("operazione", scelta)
            targa = input("targa:")
            punto2(GV, targa)

        case '3':
            print("operazione", scelta)
            targa = input("targa:")
            punto3(GV, targa)

        case '4':
            print("operazione", scelta)
            punto4(GV)

        case '5':
            print("operazione", scelta)
            punto5(GV)
        case '6':
            print("operazione", scelta)
            punto6(GV)
        case '0':
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
