import random
psw = 'purple1'
rock = open('C:/Users/ICTS22-24.016/Downloads/rockyou.txt', 'r')
for line in rock:
    tmp = rock.readline()
    if psw == tmp:
        print("sono dentro")
