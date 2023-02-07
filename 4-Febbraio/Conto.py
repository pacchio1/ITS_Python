class ContoCorrente:
    numconti=0
    def __init__(self,saldo) -> None:
        self.__salde=saldo
        ContoCorrente.numconti +=1
        self.__numconto=ContoCorrente.numconti
        self.__movimenti=[]
        self.__proprietario=None
    def getSaldo(self):
        return self.__salde
    def setSaldo(self,saldo):
        self.__salde=saldo
    def getNC(self):
        return self.__numconto
    def getOWN(self):
        return self.__proprietario
    def setOWN(self,prop):
        self.__proprietario=prop
    def prelievo(self,x):
        """prelievo dal conto di valore x; restituisce -1 se x e negativo 0  per successo"""
        if x<0:
            return -1
        else:
            self.__salde -=x
            self.__movimenti.append("prelievo "+str(-x))
            return 0
    def versamento(self,x):
        """versamento sul conto di x; restituisce -1 se x e negativo 0  per successo"""
        if x<=0:
            return -1
        else:
            self.__salde +=x
            self.__movimenti.append("versamento "+str(+x))
            return 0
