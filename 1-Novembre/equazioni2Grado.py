######	Marco Pacchiotti 016	######
import math
print("x1  e x2:")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
delta = (b*b) - (4*a*c)
x1 = x2 = 0
if delta == 0:
    x1 = -b/(2*a)
    print("x1 = x2 =", x1)
elif delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("X1 =", x1, "X2=", x2)

elif delta < 0:
    x1 = 0
    print("no radici")
else:
    print("out")
