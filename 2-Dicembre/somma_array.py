arr1=[1,2,3,4,5]
arr2=[1,1,2,3,4]
matrice=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
arr3=[0,0,0,0,0]
def somma(arr1,arr2):
    for x in range(0,5):
        arr3[x]=arr1[x]+arr2[x]
    return arr3
def moltiplica(arr1, arr2):
    for x in range(0,5):
        for y in range(0,5):
            if x<5 and y<5:
                #print(x,y)
                matrice[x][y]=arr1[x]*arr2[y]
            else:
                pass
    return matrice
print(somma(arr1,arr2))
print(moltiplica(arr1,arr2))
