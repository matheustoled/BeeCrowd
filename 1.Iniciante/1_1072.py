n = int(input())

lista = []
lista_in = []
lista_out = []

for i in range(n):
    x = int(input())
    lista.append(x)

for v in range(len(lista)):
    if lista[v] >= 10 and lista[v] <= 20:
        lista_in.append(lista[v])
    else:
        lista_out.append(lista[v])

for c in range(len(lista_in)):
        c += 1
        lista_in.append(c)
        del lista_in[c-1]
        lista_in.append(c)
        del lista_in[c-1]

lista_in.sort()
lista_in.reverse()

for c in range(len(lista_out)):
        c += 1
        lista_out.append(c)
        del lista_out[c-1]
        lista_out.append(c)
        del lista_out[c-1]

lista_out.sort()
lista_out.reverse()

print("{} in".format(lista_in[0]))
print("{} out".format(lista_out[0]))