######	Marco Pacchiotti 016	######
# calcola media temperature
import statistics
print("calcola media temperature")
t1 = 37.5
t2 = 40
t3 = 25.3

lista = [t1, t2, t3]
media = sum(lista)/len(lista)
print(media)

media = statistics.mean(lista)
print(f"{media:3.3f}")
