######	Marco Pacchiotti 016	######
f = input("frase da elaborare: ")
a = ""
for char in f:
    if char.isupper() == True:
        a = a+char.lower()
    else:
        a = a+char.upper()
print(a)
