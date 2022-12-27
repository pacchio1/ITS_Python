######	Marco Pacchiotti 016	######
#menu
import os
Menu="""
-------------------
    a) inserire da tastiera i dati delle auto vendute
    b) visualizzare il solo cognome degli acquirenti di auto di cilindrata superiore a 1500 cc
    c) visualizzare il numero totale di auto che sono state immatricolate in un anno richiesto
        in input all’utente.
    d) ordinare l’elenco in base all’anno di immatricolazione
    e) stampare l’elenco ordinato per anno di immatricolazione

    z)esci
-------------------
"""
scelta=-1
while scelta!=0:
    os.system("cls")
    #os.system("ping localhost")
    print(Menu)
    scelta=(input(':'))
    match scelta:
        case 'a':
            print("operazione",scelta)

        case 'b':
            print("operazione",scelta)

        case 'c':
            print("operazione",scelta)

        case 'd':
            print("operazione",scelta)

        case 'e':
            print("operazione",scelta)

        case 'z':
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
