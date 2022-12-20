array=[0 for i in range(0,50)]
import random
min=101
mas=0
tmp=0
minpos=0
j=49
def ran():
    return random.randint(20,100)


for i in range(0,50):
    array[i]=ran()
print(array)
def minore():
    return min(array)
for i in range(0,50):
    if array[i]<min:
        min=array[i]


print("il minimo è alla posizione",minpos,"con il valore",min)

for i in range(0,50):
    if array[i]>mas:
        mas=array[i]


print("il massimo è alla posizione",minpos,"con il valore",mas)

for i in range(0,50):
    tmp=tmp+array[i]


print(tmp/50)

array2=array.copy()
array3=[0 for i in range(0,50)]

print(array2)
for i in range(0,50):
    array3[i]=array[j]
    if j>-1:
        j-=1

print(array3)
