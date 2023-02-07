######	Marco Pacchiotti 016	######
#menu
import os
import math
Menu="""
-------------------
    1.+
    2.-
    3./
    4.*
    5.sqrt()
    6. **
    0.fine
-------------------
"""
scelta=-1
while scelta!=0:
    os.system("cls")
    print(Menu)
    scelta=int(input('operazione:'))
    n1=int(input('N1:'))
    
    match scelta:
        case 1:
            n2=int(input('N2:'))
            print(n1+n2)
            
        case 2:
            n2=int(input('N2:'))
            print(n1-n2)
            
        case 3:
            n2=int(input('N2:'))
            print(n1/n2)
            
        case 4:
            n2=int(input('N2:'))
            print(n1*n2)
            
        case 5:
            print(math.sqrt(n1))
        case 6:
            n2=int(input('N2:'))
            print(n1**n2)
        case 0:
            break
        case _:
            print("input sbagliato")
            
    input("premi invio per continuare")
