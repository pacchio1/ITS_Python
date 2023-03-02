###### Marco Pacchiotti 016	######
# Esercizio 3 - Mangia Vocali
"""scrivere un programma che legge in input una frase ed elimina tutte
le vocali e stampa la frase finale senza vocali
"""
a = input("inserisci frase: ")
b = ""
for i in a:
    a.lower()
    if not (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        b += i
print(b)
