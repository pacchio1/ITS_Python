######	Marco Pacchiotti 016	######
#cifrario di cesare
strChiara=input("testo da criptare:  ")
nCesare=int(input("spostamento: "))
strCript=""
for i in strChiara:
    codiceAscii=ord(i)#funzione che ritorna il codice ascii
    strCript=strCript+chr(codiceAscii+nCesare)#inverso di ord (chr)
strChiara=""
print(strCript)
for i in strCript:
    codiceAscii=ord(i)-nCesare
    strChiara=strChiara+chr(codiceAscii)
print(strChiara)