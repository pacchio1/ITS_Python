
# ________ stinghe __________
import math
a = "La mia prima stringa, in doppie virgolette"
print(a)
# Questo modo è equivalente al precedente.
print("---------")
b = 'la mia seconda stringa, in virgolette singole'
print(b)
print("---------")
# Tre doppie virgolette, su più linee
c = """la mia terza stringa
in triple doppie virgolette
quindi la posso mettere
su più righe"""
print(c)
print("---------")
# Tre apici, su più linee
d = '''la mia quarta stringa,
in tripli apici
può pure essere messa
su più linee
'''
print(d)
print("\t --------- \n")  # sequenze escape

print(len(a))  # lunghezza di una stringa
# iserire caratteri speciali in stringa
# se c'è un solo apice ed è tra doppie visgolette non serve usare \
stringa = "Così metto \'apici\' e \"doppie virgolette\" nelle stringhe"
print(stringa)
# inserire in una stringa caratteri speciali Unicode
print("\n----\n questa è una stella unicode \u272A")
# ______________ numeri _________
x = 3
print("\n Ho saltato %s volte" % x)
x = 3
y = 5
premio = 'Migliore Atleta della Valle'
print("\nHo saltato %s volte, fatto %s flessioni e vinto il premio '%s'" %
      (x, y, premio))
print("\nHo saltato", x, "volte, fatto", y,
      "flessioni e vinto il premio '", premio, "'")
# estrae una sottostringa a partire dalla posizione 9 alla posizione 14
st = premio[9:15]
print(st)
print(premio[4:5])  # estrae solo il carattere alla posizione 4

print("leta" in premio)
# _________ NUMEri Reali arrotondamento ____
# numeri reali e arrotondamenti del processore
# secondo lo standard IEEE-754 floating point arithmetic
# questo impone un limite fisico alla precisione dei numeri,
# e a volte possono anche capitare sorpese dovute alla conversione da decimale a binario
x = 4.1
print(x)
#nnumero in memoria
print(format(x, '.55f'))  # stampa con 55 cifre decimali
#
y = 7.9 - 3.8
print("y=", y)
print(format(y, '.55f'))  # stampa con 55 cifre decimali

# evitare di usare == con i float
print("y==4.1 ->", y == 4.1)
if y == 4.1:
    print("uguali")
else:
    print("diversi")

# per sapere se due numeri reali sono uguali conviene usare math.isclose()
#  math.isclose usa una precisione di 1e-09 ma si può indicare una diversa
print(math.isclose(y, 4.1, abs_tol=0.000001))
print(math.isclose(y, 4.1))
