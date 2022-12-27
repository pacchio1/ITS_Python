"""ESERCIZIO –Altezza delle Persone
Scrivi un programma per caricare in memoria una struttura dati per conservare i nomi e l’altezza di
persone. Scegliere l’altezza con una funzione random (altezze tra 50 e 210 cm)
Utilizzare i numeri random per caricare i dati
Realizzare le seguenti funzioni:
1. Calcolare quale è la persona più alta di tutto l’elenco e stampare
2. Calcolare la persona più bassa di tutto l’elenco
3. Dato un nome di persona stampare la sua altezza
4. Data una altezza stampare l’elenco delle persone che hanno quella altezza
5. Ordinare l’elenco in ordine crescente di altezza
6. Stampare elenco con nomi e altezze
Utilizzare le funzioni e un menu per realizzare l’applicazione e usare un dizionario per
conservare i dati."""
persona=[]
persone=[]

import random
def ran():
  return random.randint(50,210)

while True:
  nome=input("nome:")
  altezza=ran()
  persona.append(nome)
  persona.append(altezza)
  persone.append(persona)
  scelta=input("1 per uscire")
  if scelta=='1':
    break
print(persone)
x=input("altezza da ricercare")
for item in persone:
  if x=persone[]
