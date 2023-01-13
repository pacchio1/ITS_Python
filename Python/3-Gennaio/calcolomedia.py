classe={}
voti=[]
ragazo={"nome":"mario",'cognome':'rossi'}
import random
def ran():
    return random.randint(4,10)
for i in range (0,31):
    for i in range(0,4):
        voti.append(ran())
    ragazo.update({'voti':voti})
    voti=[]
    classe.update({i:ragazo})

print(classe)
