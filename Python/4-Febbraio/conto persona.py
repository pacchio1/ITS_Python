from Persona import Persona
from Conto import ContoCorrente
p1=Persona ("mario","rossi")
c1=ContoCorrente(500)
print(p1,c1)
p1.setConto(c1)
c1.setOWN(p1)

print(c1.getOWN(),p1,"conto:",p1.getConto)
val=float(input("valore da prelevare"))
rit=c1.prelievo(val)
if rit==0:
    print("effetuato:",val,"nuovo saldo:",c1.getSaldo())
elif rit==-1:
    print("errore")

val=float(input("valore da ritirare"))
rit=c1.versamento(val)
if rit==0:
    print("effetuato:",val,"nuovo saldo:",c1.getSaldo())
elif rit==-1:
    print("errore")
