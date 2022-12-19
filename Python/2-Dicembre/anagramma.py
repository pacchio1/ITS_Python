str1="marco"
str2="ouram"
i=0
j=0
str1.split
str2.split
flag=False
while True:
    if len(str2)<j:
        print("non anagrammi")
        break
    elif flag:
        print("anagrammi")
        break
    if str1[i]==str2[j]:
        j+=1
        i=0
        if len(str2)==j:
            flag=True
    else:
        i+=1



