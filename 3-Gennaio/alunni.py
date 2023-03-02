###### Marco Pacchiotti 016	######

import os
from tkinter import filedialog
# metodi


def read_file(nome_file):
    # print(nome_file)
    stream = open(nome_file, mode="r", encoding="utf-8")
    st = stream.read()
    print(st)
    stream.close()


def write_file(st):
    stream = open(
        "C:/Users/ICTS22-24.016/Documents/GitHub/Pyton_its/test_file.txt", "ab")
    stream.writelines(st+"\n")
    stream.close()


# variabili globali
nome_file = "C:/Users/ICTS22-24.016/Documents/GitHub/Pyton_its/test_file.txt"
Menu = """
+-----------------------+
|    1.aggiungi alunno  |
|    2.leggi e stampa   |
|                       |
|    0.fine             |
+-----------------------+
"""
scelta = -1
# main
while scelta != 0:
    os.system("cls")
    print(Menu)
    scelta = int(input(':'))
    match scelta:
        case 1:
            print("operazione", scelta)
            while True:
                try:
                    nome_alunno = input("nome_alunno:")
                    media = float(input("Media:"))
                    # promosso = (input("Promosso si/no:"))
                    """
                    if promosso=='si':
                        promosso=True
                    elif promosso=='no':
                        promosso=False
                    else:
                        raise(print("prosso accetta solo si o no"))
                    """

                    if media >= 1 and media <= 10:
                        if media >= 6:
                            promosso = 'p'
                        else:
                            promosso = 'r'
                    else:
                        raise (print("media furi dal intervallo"))
                    break
                except:
                    print("errore")
            st = nome_alunno, media, promosso
            write_file(str(st))

        case 2:
            print("operazione", scelta)
            read_file(nome_file)

        case 0:
            break
        case _:
            print("input sbagliato")

    input("premi invio per continuare")
