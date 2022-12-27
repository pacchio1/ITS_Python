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
acquirente=[]
auto=[]
autosalone=[]
scelta=-1
while scelta!=0:
    os.system("cls")
    #os.system("ping localhost")
    print(Menu)
    scelta=(input(':'))
    match scelta:
        case 'a':
            print("operazione",scelta)
            marca=input("marca:")
            cilindrata=int(input("cilindrata:"))
            anno_imm=input("anno di immatricolazione:")
            nome_acq=input("acquirente nome:")
            cognome_acq=input("acquirente cognome:")
            acquirente.append(nome_acq)
            acquirente.append(cognome_acq)

            auto.append(marca)
            auto.append(cilindrata)
            auto.append(anno_imm)
            auto.append(acquirente)

            autosalone.append(auto)
            print(autosalone)

        case 'b':
            print("*"*10,"auto di cilindrata superiore a 1500 cc","*"*10)
            for i in range(0,len(autosalone)-1):
                #print(i)
                if (autosalone[i][1])>1500:
                  #print(str(autosalone[i][3]))
                  acquirente=autosalone[i][3]
                  print(acquirente[1])

        case 'c':
           print("*"*10,"numero totale di auto che sono state immatricolate in un anno richiesto","*"*10)

        case 'd':
            print("operazione",scelta)

        case 'e':
            print("operazione",scelta)

        case 'z':
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
