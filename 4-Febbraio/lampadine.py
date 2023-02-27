import os


class lampadina:
    def __init__(self):
        self.__accesa = False
        self.__rotta = False
        self.n_cilcli_accensione = 5

    def rotta(self):
        if self.n_cilcli_accensione == 0:
            self.__rotta = True
            self.__accesa = False

    def click(self):
        if self.__accesa == False and self.__rotta == False:
            self.__accesa = True
        else:
            self.__accesa = False
        self.n_cilcli_accensione = self.n_cilcli_accensione-1

    def __str__(self) -> str:
        return "accesa= "+str(self.__accesa)+" rotta= "+str(self.__rotta)


philips = lampadina()
print(philips.__str__())
###### Marco Pacchiotti 016	######
# menu
Menu = """
-------------------
    1 - Accendi/Spegni Lampadina
    2 - stampa stato della lampadina
    3 - crea nuova lampadina


    0 - exit
-------------------
"""
scelta = -1
while scelta != 0:
    os.system("cls")
    print(Menu)
    scelta = (input(':'))
    match scelta:
        case '1':
            print("operazione", scelta)
            philips.rotta()
            philips.click()
            print("modifificato lo stato della lampadina")
        case '2':
            print("operazione", scelta)
            print(str(philips))
        case '3':
            print("operazione", scelta)
            philips = lampadina()
        case '0':
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
