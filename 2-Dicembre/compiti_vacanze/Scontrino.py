###### Marco Pacchiotti 016	######
# menu
def sconto(n,perc):
    print("totale:",n,"€ sconto aplicabile di:",n*(perc/100),"€")
    return n-(n*(perc/100))
import os
spesa = []
articolo = []
sconto_a=0
flag=False
Menu = """
-------------------
    1.Inserimento dati 1
    2.Applica Sconto 2
    3.Stampa scontrino 3

    0.fine
-------------------
"""
scelta = -1
while scelta != 0:
    os.system("cls")
    print(Menu)
    scelta = int(input(':'))
    match scelta:
        case 1:
            print("operazione", scelta)
            while True:
                try:
                    nome = input("Nome prodotto:")
                    prezzo = float(input("Prezzo:"))
                    quantita = int(input("Quantita:"))
                    break
                except:
                    print("errore")
            articolo.append(nome)
            articolo.append(prezzo)
            articolo.append(quantita)
            spesa.append(articolo)
            flag=True
        case 2:
            print("operazione", scelta)  # spesa=[['nome', prezzo, quantita]]
            if flag==True:
                for i in range(0, len(spesa)):
                    totale=spesa[i][1]*spesa[i][2]
                    if totale>=50.0 and spesa[i][2]>5:
                        print("sconto del 2% per totale >= 50 €",totale)
                        totale=sconto(totale,2)
                        print("sconto del 7% per 5 o piu articoli uguale/i",totale)
                        totale=sconto(totale,7)
                        print("per un totale di",totale)
                        sconto_a=7
                    elif totale>=50.0:
                        print("sconto del 2% per totale >= 50 €",totale)
                        totale=sconto(totale,2)
                        print("per un totale di",totale)
                        sconto_a=2
                    else:
                        print(totale)
        case 3:
            print("operazione", scelta)
            print("ARTICOLO     PREZZO      QUANTITA’       SCONTO APPLICATO        TOTALE SCONTATO")
            if flag==True:
                for i in range(0, len(spesa)):
                          #"ARTICOLO     PREZZO      QUANTITA’       SCONTO APPLICATO        TOTALE SCONTATO"
                    print(str(spesa[i][0]),"        ",str(spesa[i][1]),"        ",str(spesa[i][2]),"          ",str(sconto_a),"                    ",totale)

        case 0:
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
