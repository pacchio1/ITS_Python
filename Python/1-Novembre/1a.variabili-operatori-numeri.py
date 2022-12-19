# numeri
i = 11234  # intero undicimiladuecentotrentaquattro
a = 0O23  # ottale 23
ex = 0X123  # esadecimale 123
bin = 0b11111111         # binario
print(i, 11_111, a, ex, bin, sep='\t')

# numeri decimali float
c = 4.0
d = 3E2  # 3 x 10^2 =300.0
f = 3e2
# velocità della luce 3E8
print(c, d, f)

# nomi delle variabili
# no spazi, non inizio con numeri, non con nomi di parole chiavi

# string  usare " dentro le stringhe, si usa mettere \ davanti
print("I like \"Monty Python\"")
print('I like "Monty Python"')
# string  usare ' dentro le stringhe
print('I\'m Monty Python.')
# oppure
print("I'm Monty Python.")

# boolean
g = 1
print(g == 1)

#operatori + (somma) - (sottrazione) * (motiplizazione) / (divisione)
# // (divisione intera) % (modulo) (resto divisione intera) ** (esponinziazione)

print(9/2, 9//2, 9 % 2, 9**2, sep='\t')

# conversione numeri in stringa -> funzione str() e operatore +
h = "-"+str(c)+"-"
print(h)
# conversione stringhe in numeri int(), float()

a1 = int(input("inserisci un numero:"))
a2 = a1*3
print(a2)

a1 = input("inserisci un numero:")
print(float(a1))
a2 = a1*3  # operatore * applicato alle stringhe
print(a2)
