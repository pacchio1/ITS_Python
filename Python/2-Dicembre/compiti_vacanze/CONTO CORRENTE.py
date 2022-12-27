######	Marco Pacchiotti 016	######
#menu
import os
saldo=100.0
ultimomovimento="non ci sono ancora stati movimenti"
Menu="""
-------------------
    1. Saldo
    2. Prelievo
    3. Versamento
    4. Stampa ultimo movimento

    0. Fine
-------------------
"""
scelta=-1
while scelta!=0:
    os.system("cls")
    #os.system("ping localhost")
    print(Menu)
    scelta=int(input(':'))
    match scelta:
        case 1:
            print("saldo",scelta)
            print()
            print("saldo disponibile:",saldo)

        case 2:
            print("prelievo",scelta)
            print("quanti soldi si desidera prelevare slado corennte pari a:",saldo)
            prelievo=float(input(":"))
            if saldo>prelievo and prelievo>0:
                saldo=saldo-prelievo
            else:
                print("lo sconfinamento del conto viene effettuato al tasso del 20 percento di interesse s=Si per accetare lo sconfinamento")
                scelta=(input())
                if scelta=='s' or scelta =='S':
                    saldo=saldo-prelievo
                    saldo=saldo-(saldo*0.20)
            print(saldo)
            ultimomovimento="prelievo di: "+str(prelievo)

        case 3:
            print("versamento",scelta)
            while True:
                try:
                    versamento = int(input("inserire inporto:"))
                    if versamento>0:
                        break
                    else:
                        print("il valore deve essere maggiore di zero")
                        continue
                except:
                    print("errore")
            saldo=saldo+versamento
            print("versamento riuscito di",versamento,"per un totale di",saldo)
            ultimomovimento="versamento di: "+str(versamento)

        case 4:
            print("ultimo movimento",scelta)
            print(ultimomovimento)
        case 0:
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
