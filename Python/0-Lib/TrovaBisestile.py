######	Marco Pacchiotti 016	######
print("calcola bisestile, inserisci anno:")
anno = int(input())
if anno < 1582:
    print("non anno calendario gregoriano")
else:
    if anno % 4 != 0:
        print("anno non bisestile")
    elif anno % 100 != 0:
        print("anno bisestile!")
    elif anno % 400 != 0:
        print("anno non bisestile!")
    else:
        print("anno bisestile!")
