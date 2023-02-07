import random
psw = 'purple1'
rock = open('C:/Users/ICTS22-24.016/Documents/GitHub/Pyton_its/Python/Z-Prove/miniRock.txt', 'r')
i=1;
for line in rock:
    if psw == line.strip():
        print("sono dentro password:",line,"trovato in pos:",i)
    i=i+1
