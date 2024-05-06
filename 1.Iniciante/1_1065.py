a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
valores = [a,b,c,d,e]
pares = []
lista = []

for i in range(0,5):
    if valores[i]%2 == 0:
        pares.append(valores[i])

for c in range(len(pares)):
    c = c + 1
    lista.append(c)

lista.sort()
lista.reverse()

print("{} valores pares".format(lista[0]))
