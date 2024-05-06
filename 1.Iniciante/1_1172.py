valores = []

for i in range(0,10):
    x = int(input())
    valores.append(x)

for v in range(len(valores)):
    if valores[v] == 0:
        valores[v] = 1
    elif valores[v] < 0:
        valores[v] = 1

for p in range(len(valores)):
    print("X[{}] = {}".format(p,valores[p]))

