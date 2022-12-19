import random
def ran():
    return random.randint(0,9)
matrix = [[0 for i in range(0,5)] for j in range(0,5)]
somma=[0,0,0,0,0]
for x in range(0,5):
    for y in range(0,5):
        if x<5 and y<5:

            matrix[x][y]=ran()
        else:
            pass
for x in range(0,5):
    print(matrix[x][0],matrix[x][1],matrix[x][2],matrix[x][3],matrix[x][4])
def somma_rige(matrix):

    for x in range(0,5):
        somma[x]=matrix[x][0]+matrix[x][1]+matrix[x][2]+matrix[x][3]+matrix[x][4]
    return somma
print(somma_rige(matrix))
def somma_colonne(matrix):

    for x in range(0,5):
        somma[x]=matrix[0][x]+matrix[1][x]+matrix[2][x]+matrix[3][x]+matrix[4][x]
    return somma
print(somma_colonne(matrix))
