######	Marco Pacchiotti 016	######
import os
strChiara=""
nCesare=0
strCript=""
Menu="""
-------------------
    1.inserisci testo da criptare
    2.decripta testo
    
    3.fine    
-------------------
"""
scelta=-1
while scelta!=0:
    os.system("cls")
    print(Menu)
    scelta=int(input(':'))
    match scelta:
        case 1:
            strChiara=""
            strCript=""
            strChiara=input("testo da criptare:  ")
            nCesare=int(input("spostamento: "))
            for i in strChiara:
                codiceAscii=ord(i)#funzione che ritorna il codice ascii
                strCript=strCript+chr(codiceAscii+nCesare)#inverso di ord (chr)
            print(strChiara)
            print(strCript)
            strChiara=""           
        case 2:
            for i in strCript:
                codiceAscii=ord(i)-nCesare
                strChiara=strChiara+chr(codiceAscii)
            print(strChiara)
            
        case 3:
            break
        case _:
            print("input sbagliato")         
    input("premi invio per continuare")


