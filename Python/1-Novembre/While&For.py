######	Marco Pacchiotti 016	######

'''
numero=int(input("inserisci un numero o-1 per terminare: "))
mas=numero
contatore=0
while numero !=-1:
    contatore +=1
    numero=int(input("inserisci un numero o-1 per terminare: "))
    if numero ==15:
        continue
    if mas<numero:
        mas=numero
    if contatore>=9:
        break
print(str(mas))
'''
#### for####
for i in range(0, 6):
    if i == 3:
        pass  # pass != continue
        # break
    print("i :", i)
else:
    print("finito il for")
lista = [2, 4, 6]
for i in lista:
    print("valore i=")
