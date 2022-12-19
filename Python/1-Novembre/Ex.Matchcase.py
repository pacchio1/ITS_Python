######	Marco Pacchiotti 016	######
# utilizzo della struttura match -case === switch
n = input("inserisci valore ")
match n:
    case'1':
        print("ciao")
    case'2':
        print("hey")
    case '3' | '4':
        print("whow")
    case _:
        print("hola")
n = int(input("inserisci valore "))
match n:
    case 1:
        print("ciao")
    case 2:
        print("hey")
    case 4:
        print("whow")
    case _:
        print("hola")
