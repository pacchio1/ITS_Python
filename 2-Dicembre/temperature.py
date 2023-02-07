def convertiTemp(K, tipo):
    
    if tipo ==1:
        K=int(K) - 273.15
        return str(K) +"°C"
    #in celsius
    if tipo ==0:
        K= int(K) + 273.15
        return str(K) +"K"
    #in Kelvin
while True:
    K=input("inserire temperatura (lettera per uscire):")
    tipo=int(input("inserire 0per celsius, 1 Kelvin:"))
    if K.isdigit():
        print(convertiTemp(K,tipo))
        
    else:
        print("sei uscito dal programma:")
        break