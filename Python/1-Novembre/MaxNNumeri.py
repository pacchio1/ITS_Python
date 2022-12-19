######	Marco Pacchiotti 016	######
print("inserisci 3 numeri")
a = input()
b = input()
c = input()
if a.isdigit() == True and b.isdigit() == True and c.isdigit() == True:
    print("max :", str(max(a, b, c)))
else:
    print("errore nei parametri")
