######	Marco Pacchiotti 016	######
#menu
import os
import random
Menu="""
-------------------
    1) Inserimento dati delle squadre
    2) Stampare la classifica delle squadre in ordine decrescente di punteggio
    3) Modificare i punti di una squadra con input da tastiera
    4) Stampare classifica titoli degli allenatori in ordine decrescente di titoli
    5) Numero totale di allenatori che hanno vinto Y titoli , con Y preso in input.
    6) Stampa squadre con più di Y punti in classifica (Y preso in input)
    7) Stampare squadre con allenatori che hanno vinto più di Y titoli (Y preso in input).
    0.fine
-------------------
"""
def ran():
    return random.randint(0,50)
squadre=[["team1", "red", 10, "coach1"], ["team2", "blue", 5, "coach2"], ["team3", "green", 15, "coach3"]]
allenatori= [[" Rossi", "Mario", 10, "Juventus"], ["Bianchi", "Paolo", 20, "Inter"], ["Neri", "Luca", 15, "Juventus"]]
flag=False
def Inserisci_Squadre(squadre):

    while True:
        try:
            nome=input("Nome squadra:")
            coloremaglia=input("colore maglia:")
            punteggio=int(input("punteggio"))
            nome_alenatore=input("Nome della alenatore")
            break
        except:
            print("errore")
    squadre.append([nome,coloremaglia,punteggio,nome_alenatore])
def matrice_ordinataXPunti(squadre) :
    sorted_teams = sorted(squadre, key=lambda x: x[2], reverse=True)
    return sorted_teams
def stampaClassifica(squadre):
    i=0
    sorted_teams= matrice_ordinataXPunti(squadre)
    while i<len(sorted_teams):
        tmp=sorted_teams[i]
        punteggio=tmp[2]
        nome=tmp[0]
        colore=tmp[1]
        txt = "{:.<13} {:<5} {:<10}"
        stringa=txt.format(nome, punteggio, colore)
        out(stringa)
        i=i+1
def editSquadra(squadre):
    edit=input("nome squadra da modificare:")
    for i in range(len(squadre)):
        if squadre[i][0] == edit:
            while True:
                try:
                    n = int(input("numero di punti da sommare:"))
                    break
                except:
                    print("errore")

            squadre[i][2] += n
            s=squadre[i][2]+n
            st="team: "+edit+" atuali punti: "+str(s)
            out(st)
            break

        else:
            print("squadra non trovata")
def ordinaAllenatori(allenatori):
    allenatori.sort( key=lambda x: x[2], reverse=True)
    return allenatori
def allenatoriXtitoli(allenatori):
    i=0
    ordinata=ordinaAllenatori(allenatori)
    while i < len(ordinata):
        tmp=ordinata[i]
        cognome=tmp[0]
        nome=tmp[1]
        punteggio=tmp[2]
        squadra=tmp[3]
        txt = "{:.<13} {:<13} {:<13} {:<13}"
        stringa=txt.format(cognome, nome, punteggio, squadra)
        out(stringa)
        i=i+1
def allenatoriContotPunti(allenatori):
    i=0
    j=0
    y=input("punteggio da cercare:")

    while i<len(allenatori):
            if allenatori[i][2] == int(y):
                j += 1
            i=i+1
    stringa="Il numero totale di allenatori che hanno vinto " + str(y) + " titoli è: " + str(j)
    out(stringa)

def stampaClassifica2(Q):
    i=0
    ordinata= matrice_ordinataXPunti(squadre)
    while i < len(ordinata):
        tmp=ordinata[i]
        punteggio=tmp[2]
        nome=tmp[0]
        txt = "{:.<13} {:<5}"
        stringa=txt.format(nome, punteggio)
        #print(Q)
        if punteggio>=int(Q):
            out(stringa)
        i=i+1
def alenatoripiudiToTtitoli(allenatori):
    i=0

    search=input("punteggio da cercare:")
    while i<len(allenatori):
        tmp=allenatori[i]
        #print(tmp)
        squadra=tmp[3]
        nome=tmp[1]
        cognome=tmp[0]
        titoli=tmp[2]

        txt = "{:.<13} {:<13} {:<13} {:<13}"
        stringa=txt.format(squadra,cognome ,nome ,titoli)
        if tmp[2]>=int(search):
                out(stringa)

        i=i+1
def out(stringa):
    print(stringa)
scelta=-1
while scelta!=0:
    os.system("cls")
    print(Menu)
    scelta=(input(':'))
    match scelta:
        case '1':
            print("Inserimento dati delle squadre",scelta)
            Inserisci_Squadre(squadre)




        case '2':
            print("operazione",scelta)
            stampaClassifica(squadre)

        case '3':
            print("operazione",scelta)
            editSquadra(squadre)

        case '4':
            print("operazione",scelta)
            allenatoriXtitoli(allenatori)

        case '5':
            print("operazione",scelta)
            allenatoriContotPunti(allenatori)

        case '6':
            print("operazione",scelta)
            while True:
                try:
                    Q=int(input("numero min punti"))
                    break
                except:
                    print("errore")

            stampaClassifica2(Q)

        case '7':
            print("operazione",scelta)
            alenatoripiudiToTtitoli(allenatori)

        case '0':
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
