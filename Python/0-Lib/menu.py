######	Marco Pacchiotti 016	######
#menu
import os
Menu="""
-------------------
    1.opzione 1
    2.opzione 2
    3.opzione 3
    4.opzione 4
    5.opzione 5
    0.fine
-------------------
"""
scelta=-1
while scelta!=0:
    os.system("cls")
    #os.system("ping localhost")
    print(Menu)
    scelta=int(input(':'))
    match scelta:
        case 1:
            print("operazione",scelta)
            
        case 2:
            print("operazione",scelta)
            
        case 3:
            print("operazione",scelta)
            
        case 4:
            print("operazione",scelta)
            
        case 5:
            print("operazione",scelta)
            
        case 0:
            break
        case _:
            print("input sbagliato")
            
    input("premi invio per continuare")
