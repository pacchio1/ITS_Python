######	Marco Pacchiotti 016	######
s1 = "bjckdjflanoe3psanloperanoianta"
s2 = input(":")
flag=True
start = end = 0
for i in s2:
    start = s1.find(i, start)
    if start != -1:
        print("la lettera e stata trovata al caratere:", start)
    else:
        print("caratere non trovato")
        flag=False
if flag==True:
    print("tutta la parola/frase e stata trovata")
else:
     print("non tutta la parola/frase e stata trovata")