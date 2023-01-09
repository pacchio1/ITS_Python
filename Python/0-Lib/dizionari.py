dizionario={"dog":"cane","horse":"cavalllo",'cat':'gatto'}
dizionario["cat"]='gatto'
dizionario.update({'carrot':"carota"})
parole=['cat','dog','mouse']
print (dizionario)
for p in sorted(dizionario.keys()):
    print(p,dizionario[p])
for p in parole:
    for key in dizionario.keys():
        if p==key:
            print(key,'in dizionario',dizionario[key])
        else:
            print(p,'non nel dizionario')
