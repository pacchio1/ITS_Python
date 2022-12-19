A = int(input("Altezza in cm:"))
M = int(input("Peso:"))
"""Categoria BMI range - kg/m2
Sottopeso severo < 16,5
Sottpeso da 16,5 a 18,4
Normale da 18,5 a 24,9
Sovrappeso da 25 a 30
Obesità primo grado da 30,1 a 34,9
Obesità secondo grado da 35 a 40
Obesità terzo grado > 40"""
if M >= 10 and M < 180 and A >= 10 and A < 220:
    A = A/100
    bmi = M/(A**2)
    if bmi < 16.6:
        print("Sottopeso severo")
    elif bmi < 18.5:
        print("Sottpeso")
    elif bmi < 25:
        print("Normale")
    elif bmi < 31:
        print("Sovrappeso")
    elif bmi < 35:
        print("Obesità primo grado")
    elif bmi < 41:
        print("Obesità secondo grado")
    elif bmi > 40:
        print("Obesità terzo grado")
    print(bmi)
else:
    print("input errato")
