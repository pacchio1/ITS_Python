######	Marco Pacchiotti 016	######
print("inserire un numero x vedere se è pari o dispari")
n1 = input()
if n1.isdigit():
    n = int(n1)
    if n % 2 == 0:
        print("pari")
    else:
        print("dispari")
else:
    print("errore nel parametro")
