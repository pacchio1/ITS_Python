######	Marco Pacchiotti 016	######
import random
while True:
    choRan=random.randint(0,2)
    choUma=int(input("0 x carta 1 x sasso 2 x forbici"))
    if(choRan==choUma):
        print("pari","scelta umana: ",choUma,"scelta del pc:",choRan)
    elif(choUma==0 and choRan==2 or choUma==1 and choRan==0 or choUma==2 and choRan==1):
        print("hai perso","scelta umana: ",choUma,"scelta del pc:",choRan)
    else:
        print("hai vinto","scelta umana: ",choUma,"scelta del pc:",choRan)
    input()