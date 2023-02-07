######	Marco Pacchiotti 016	######
import random
d=input("p x pari d x dispari: ")
m1=int(input("inserisci un numero da 1 a 5: "))
m2=random.randint(0,5)
m3=m2+m1
if(d=='p'):
    if(m3%2==0):
        print("hai vinto")
    else:
        print("hai vinto")
elif(d=='d'):
    if(m3%2==0):
        print("hai perso")
    else:
        print("hai vinto")
print("il pc ha generato",m2,"tu hai inserito",m1,"per totale: ",m3)
input()