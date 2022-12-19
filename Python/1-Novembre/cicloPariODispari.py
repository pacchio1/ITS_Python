######	Marco Pacchiotti 016	######
"""
Scrivere un programma che legge una sequenza di numeri e conta quanti
numeri sono pari e quanti sono dispari. Il programma termina quando si
inserisce 0"""
# Esercizio 4 -Conta pari e dispari


numero = int(
    input("inserisci un numero per vedere se è pari o dispari 0 x uscire: "))
flag = True

while numero != 0:
    n = int(numero)
    if n % 2 == 0:
        print("pari")
    else:
        print("dispari")
    numero = int(input("inserisci un altro numero: "))
else:
    print("sei uscito dal prog")
