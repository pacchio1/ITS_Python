######	Marco Pacchiotti 016	######
import random
n_tentativi=10
n_random=random.randint(1,100)
i=1
while n_tentativi>0:
    n_ininput = int(input("prova ad indovinare il numero"))
    if n_ininput ==n_random:
        print("hai vinto!!!")
        break
    elif n_ininput<n_random:
        print("il numero è maggiore")
    elif n_ininput>n_random:
        print("il numero è minore")
    n_tentativi=n_tentativi-1
    i=i+1
print(n_random,i)
