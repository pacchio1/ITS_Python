######	Marco Pacchiotti 016	######
#calcola fattoriale
n=int(input("N:"))
i=1
r=1;
while i<n+1:
    if n!=0:
        r=r*i
        #print(r)
    else:
        r=0
    i=i+1
print(r)