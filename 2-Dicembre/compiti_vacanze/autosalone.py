######	Marco Pacchiotti 016	######i
#menu
def riordina():
    autosalone.sort(key=lambda x: x[2])
    return autosalone
def stampa():
    i=0
    while i<len(autosalone):
            print(autosalone[i][0],autosalone[i][1],autosalone[i][2],autosalone[i][3],autosalone[i][4])
            i=i+1
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
#acquirente=[]
auto=[]
#['a', 1900, 1900, 'a', 'a'],['b', 2000, 2000, 'b', 'b'],['c', 2100, 2100, 'c', 'c'],['c', 2100, 2100, 'c', 'c'],['a', 1900, 1900, 'a', 'a']
# ["Toyota", "Corolla", 2008, "Marco Neri"]
# ["Ford", "Fiesta", 2010, "Mario Rossi"]
# ["Fiat", "Punto", 2012, "Anna Bianchi"]
# ["Ford", "Mustang", 2014, "Francesca Verdi"]
autosalone=[['a', 1900, 1900, 'a', 'a'],['b', 2000, 2000, 'b', 'b'],['c', 2100, 2100, 'c', 'c'],['c', 2100, 2100, 'c', 'c'],['a', 1900, 1900, 'a', 'a']]

scelta=-1
while scelta!=0:
    os.system("cls")
    #os.system("ping localhost")
    print(Menu)
    scelta=(input(':'))
    match scelta:
        case 'a':
            #print(len(autosalone))
            print("inserire da tastiera i dati delle auto vendute")
            marca=input("marca:")
            while True:
                try:
                    cilindrata=int(input("cilindrata:"))
                    anno_immatricola=int(input("anno di immatricolazione:"))
                    break
                except:
                    print("errore")
            nome_acq=input("acquirente nome:")
            cognome_acq=input("acquirente cognome:")

            """
            auto.append(marca)
            auto.append(cilindrata)
            auto.append(anno_immatricola)
            auto.append(nome_acq)
            auto.append(cognome_acq)"""

            autosalone.append([marca,cilindrata,anno_immatricola,nome_acq,cognome_acq])
            print(autosalone)
            print("Auto aggiunta all'elenco!")
            #auto.clear()
            marca=cilindrata=anno_immatricola=nome_acq=cognome_acq=0


            #reset dati


        case 'b':

            print("*"*10,"auto di cilindrata superiore a 1500 cc","*"*10)
            i=0
            while i<len(autosalone):
                #print(i)
                if autosalone[i][1]>=1500:
                    print(autosalone[i][4])
                i=i+1



        case 'c':
            print("*"*10,"numero totale di auto che sono state immatricolate in un anno richiesto","*"*10)

            j=0
            anno_input=int(input("anno i ricerca:"))
            i=0
            while i<len(autosalone):
                #print(i)
                if (autosalone[i][2])==anno_input:
                  j=j+1
                i=i+1
            print(j)
        case 'd':
            print("*"*10," ordinare l’elenco in base all’anno di immatricolazione","*"*10)
            riordina()
        case 'e':
            print("*"*10,"  stampare l’elenco ordinato per anno di immatricolazione","*"*10)
            riordina()
            stampa()

        case 'z':
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
