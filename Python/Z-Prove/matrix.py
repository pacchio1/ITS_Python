import random

def minuscole():
    return random.randint(97, 122)


def maiuscole():
    return random.randint(65, 90)


def numeri():
    return random.randint(48, 57)


def simboli():
    return random.randrange(0, 8)

import time
sim = "$£%&?!*@-"
i = 0
passwds = []
passwd = ""
tipo=3

def caso(tipo):
    gen = 0
    if tipo == 1:
        gen = random.randint(0, 1)
    if tipo == 2:
        gen = random.randint(0, 2)
    if tipo == 3:
        gen = random.randint(0, 3)
    return gen

import os
os.system("color 02")
while True:
    
    
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
    
    i = i+1
    if i%200==0:
        print(passwd)
        i=0
        time.sleep(0.1)
input("invio x uscire")
