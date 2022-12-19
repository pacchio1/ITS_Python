### TUPLE ###
#truple elenco inmodificabile
tupla=(11,22)
tupla2=(99,88)
tupla,tupla2=tupla2,tupla
tupla=(('a',23),('b',37),('c',11),('d',29),('a',1))
print(tupla,tupla2)
print(sorted(tupla))
tupla=tupla[:-1]
print(tupla)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
### DIZIONARI ###
dict={"cat":"gatto",
      "dog":"cane",
      "horse":"cavallo"
}
telefono={
    "zio pera":"099999999",
    "marco":"01234567890",
    "mario":"15000047111",
    "matteo":"4561900182"
}
print(dict,telefono)
print(dict["dog"])
print("dog"in dict)
for key in telefono.keys():
    print(key,"->",telefono[key])
print('*'*45)
for key in sorted(telefono.keys()):
    print(key,"->",telefono[key])
