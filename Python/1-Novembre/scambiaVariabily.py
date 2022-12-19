######	Marco Pacchiotti 016	######
# scambia_variabili
print("scambia_variabili")
n1 = input("inserisci 1 numero:")
n2 = input("inserisci 2 numero:")
print('1:', n1, '|2:', n2)
tmp = n1
n1 = n2
n2 = tmp
print('1:', n1, '|2:', n2)
n1, n2 = n2, n1
print('1:', n1, '|2:', n2)
# verifica tipo di dato
print(type(n1))
