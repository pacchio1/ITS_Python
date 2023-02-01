###### Marco Pacchiotti 016	######
numero_blocchi = int(input("numero_blocchi: "))
h = 0
i = 0
lsrow = 0
while i < numero_blocchi:
    if lsrow <= i:
        h = h+1
        lsrow = i+1
        print(lsrow*"*")
        numero_blocchi = numero_blocchi-lsrow
    else:
        lsrow = 0
    i = i+1

print(h)
input()