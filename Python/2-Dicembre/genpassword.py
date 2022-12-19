import random

lunghezza = int(input("L:"))
n_password = int(input("numero pswd"))
tipo = int(input("1 solo lettere:,2 letere e numeri:,3 lettere numeri e simboli"))


def minuscole():
    return random.randint(97, 122)


def maiuscole():
    return random.randint(65, 90)


def numeri():
    return random.randint(48, 57)


def simboli():
    return random.randrange(0, 8)


sim = "$£%&?!*@-"
i = 0
passwds = []
passwd = ""


def caso(tipo):
    gen = 0
    if tipo == 1:
        gen = random.randint(0, 1)
    if tipo == 2:
        gen = random.randint(0, 2)
    if tipo == 3:
        gen = random.randint(0, 3)
    return gen


while i < n_password:
    passwd = ""
    j = 0
    while j < lunghezza:
        n = int(caso(tipo))
        match n:
            case 0:
                passwd = passwd+chr(maiuscole())
            case 1:
                passwd = passwd+chr(minuscole())
            case 2:
                passwd = passwd+chr(numeri())
            case 3:
                tmp = simboli()
                sim.split()
                passwd = passwd+sim[tmp]
        j = j+1
    passwds.append(passwd)
    print(passwd)
    i = i+1
input("invio x uscire")
