######	Marco Pacchiotti 016	######
inp=int(input("inserire un numero x vedere se è primo: "))
Primo=True
Divisori=""
if (inp/1==inp):
    for i in range(2,inp):
        if(i!=1 and inp%i==0):
            Primo=False
            Divisori=Divisori+str(i)+','
if Primo==True:
    print(inp,"è primo")
else:
    print(inp,"non è primo")
    print("i suoi divisori sono:",Divisori)
    