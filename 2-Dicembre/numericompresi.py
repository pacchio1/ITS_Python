######	Marco Pacchiotti 016	######
h=input("h:")
k=input("k:")
i=0
if h.isdigit() and k.isdigit():
    max=h
    min=k
    if k>h:
        k=max
        h=min
    while True:
        N=input("inserire a x uscire ||| N:")
        if N=='a':
            print(i)
            break
        if int(N)>=int(min) and int(N)<=int(max):
            i=i+1
            print("N compreso tra h e k")
        else:
            print("non compreso tra h e k")