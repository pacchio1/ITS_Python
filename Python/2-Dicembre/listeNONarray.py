#elenco di persone con propri dati
def carica_elenco(persone):
    while True:
        persona=[]
        nome=input("nome:")
        cognome=input("cognome:")
        datanascita=input("data nascita:")
        sesso=input("sesso:")
        persona.append(nome)
        persona.append(cognome)
        persona.append(datanascita)
        persona.append(sesso)
        persone.append(persona)
        scelta=input("vuoi continuare 1:")
        if scelta!="1":
            break
    return persone
def stampa(elenco):
    for i in range(len(elenco)):
        print(elenco[i])
def main():
    elenco=[]
    elenco=carica_elenco(elenco)
    carica_elenco(elenco)
    stampa(elenco)
main()
