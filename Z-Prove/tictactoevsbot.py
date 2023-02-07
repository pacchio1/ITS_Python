import random
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tic = 1
tac = 2
epty = 0
flag = True
cordinata = ""
i = 0
while flag and i < 9:
    

    if i % 2 == 0:
        for x in range(0, 2):
            print(board[x][0], board[x][1], board[x][2])
        print(board[2][0], board[2][1], board[2][2])
        # turno dei tic
        cordinata = input()
        
        cordinata.split()

        if board[int(cordinata[0])-1][int(cordinata[1])-1] == 0:
            board[int(cordinata[0])-1][int(cordinata[1])-1] = tic
            i = i+1
    else:
        # turno dei tac
        cordinata = str(random.randint(1,3))+str(random.randint(1,3))
        cordinata.split()
        if board[int(cordinata[0])-1][int(cordinata[1])-1] == 0:
            board[int(cordinata[0])-1][int(cordinata[1])-1] = tac
            i = i+1
    for j in range(0, 2):
        #tris in orizontale
        if board[j][0] == board[j][1] == board[j][2] != 0:
            flag = False
            if board[j][0] == tic:
                print("tic ha vinto")
            elif board[j][0] == tac:
                print("tac ha vinto")
    for j in range(0, 2):
        #tris in verticale
        if board[0][j] == board[1][j] == board[2][j] != 0:
            flag = False
            if board[0][j] == tic:
                print("tic ha vinto")
            elif board[0][j] == tac:
                print("tac ha vinto")
    if board[0][0] == board[1][1] == board[2][2] != 0:
        flag = False
        if board[0][0] == tic:
            print("tic ha vinto")
        elif board[0][0] == tac:
            print("tac ha vinto")
    if board[0][2] == board[1][1] == board[2][0] != 0:
        flag = False
        if board[1][1] == tic:
            print("tic ha vinto")
        elif board[1][1] == tac:
            print("tac ha vinto")

for x in range(0, 2):
    print(board[x][0], board[x][1], board[x][2])
print(board[2][0], board[2][1], board[2][2])
