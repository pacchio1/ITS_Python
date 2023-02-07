Setimanale="10,5,15"
Mensile="30,20,40"
Annuale="250,150,300"
durata=input("durata:")
tipo=input("tipo:")
r=0
priorita=input("priorita s/n")
if durata=='S':
    o=Setimanale.split(',')
    if(tipo=='1'):
        r=o[0]
    if(tipo=='2'):
        r=o[1]
    if(tipo=='3'):
        r=o[2]
if durata=='M':
    o=Mensile.split(',')
    if(tipo=='1'):
        r=o[0]
    if(tipo=='2'):
        r=o[1]
    if(tipo=='3'):
        r=o[2]
if durata=='A':
    o=Mensile.split(',')
    if(tipo=='1'):
        r=o[0]
    if(tipo=='2'):
        r=o[1]
    if(tipo=='3'):
        r=o[2]
print(r)
if priorita=='s':
    r_inf=float(r)
    r_inf=r_inf-r_inf*0.2
    print(r_inf)

        
