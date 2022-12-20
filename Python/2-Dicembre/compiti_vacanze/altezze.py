import random

# Struttura dati per conservare i nomi e l'altezza delle persone
people = []

# Funzione per scegliere l'altezza di una persona con un numero casuale
def choose_height():
  return random.randint(50, 210)

# Funzione per caricare i dati delle persone nella struttura dati
def load_people(names):
  for name in names:
    height = choose_height()
    person = (name, height)
    people.append(person)

# Funzione per trovare la persona più alta dell'elenco
def find_tallest():
  tallest = people[0]
  for person in people:
    if person[1] > tallest[1]:
      tallest = person
  return tallest

# Funzione per trovare la persona più bassa dell'elenco
def find_shortest():
  shortest = people[0]
  for person in people:
    if person[1] < shortest[1]:
      shortest = person
  return shortest

# Funzione per trovare l'altezza di una persona dato il suo nome
def find_height(name):
  for person in people:
    if person[0] == name:
      return person[1]
  return "Persona non trovata"

# Funzione per trovare le persone con una determinata altezza
def find_by_height(height):
  result = []
  for person in people:
    if person[1] == height:
      result.append(person[0])
  return result

# Funzione per ordinare l'elenco in ordine crescente di altezza
def sort_by_height():
  people.sort(key=lambda x: x[1])

# Funzione per stampare l'elenco delle persone con i loro nomi e altezze
def print_people():
  for person in people:
    print(f"{person[0]}: {person[1]} cm")

# Carichiamo alcune persone nella struttura dati
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
load_people(names)

# Stampiamo la persona più alta dell'elenco
tallest = find_tallest()
print(f"La persona più alta è {tallest[0]} con {tallest[1]} cm di altezza")

# Stampiamo la persona più bassa dell'elenco
shortest = find_shortest()
print(f"La persona più bassa è {shortest[0]} con {shortest[1]} cm di altezza")

# Chiediamo all'utente il nome di una persona e stampiamo la sua altezza
name = input("Inserisci il nome di una persona: ")
height = find_height(name)

