######	Marco Pacchiotti 016	######
#menu
import os
spesa=[]
articolo=[]
Menu="""
-------------------
    1.Inserimento dati 1
    2.Applica Sconto 2
    3.Stampa scontrino 3

    0.fine
-------------------
"""
scelta=-1
while scelta!=0:
    os.system("cls")
    print(Menu)
    scelta=int(input(':'))
    match scelta:
        case 1:
            print("operazione",scelta)
            while True:
                try:
                    nome = input("Nome prodotto:")
                    prezzo=float(input("Prezzo:"))
                    quantita = int(input("Quantita:"))
                    break
                except:
                    print("errore")
            articolo.append(nome)
            articolo.append(prezzo)
            articolo.append(quantita)
            spesa.append(articolo)
        case 2:
            print("operazione",scelta)#spesa=[['N', 12.0, 3]]
            for i in range(0,len(spesa)):
                print(spesa[0][2])

        case 3:
            print("operazione",scelta)


        case 0:
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")

