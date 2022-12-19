######	Marco Pacchiotti 016	######
p1 = int(input("ponte1: "))
p2 = int(input("ponte2: "))
p3 = int(input("ponte3: "))
p4 = int(input("ponte4: "))
p5 = int(input("ponte5: "))
trag1 = p1
if p2 < trag1:
    trag1 = p2
print(str(trag1)+"T")
trag2 = p1
if p3 < trag2:
    trag2 = p3
if p4 < trag2:
    trag2 = p4
print(str(trag2)+"T")
trag3 = p1
if p5 < trag3:
    trag3 = p5
print(str(trag3)+"T")
n1 = trag1
n2 = trag2
n3 = trag3
a = [n1, n2, n3]
a.sort()
print(a[2], 'tonnellate massime')
