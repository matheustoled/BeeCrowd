n = int(input())

pares = []
potencia_pares = []

for i in range(0,n+1):
    i += 1
    if i%2 == 0:
        pares.append(i)

for q in range(len(pares)):
    x = pares[q]**2
    potencia_pares.append(x)

for p in range(len(pares)):
    print("{}^2 = {}".format(pares[p], potencia_pares[p]))