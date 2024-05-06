lista = []
pares = []
impares = []
positivos = []
negativos = []

for t in range(0,5):
    x = int(input())
    lista.append(x)

for i in range(len(lista)):
    if lista[i]%2 == 0:
        pares.append(lista[i])
    if lista[i] > 0:
        positivos.append(lista[i])
    if lista[i] < 0:
        negativos.append(lista[i])
    if lista[i]%2 != 0:
        impares.append(lista[i])

print("{} valor(es) par(es)".format(len(pares)))
print("{} valor(es) impar(es)".format(len(impares)))
print("{} valor(es) positivo(s)".format(len(positivos)))
print("{} valor(es) negativo(s)".format(len(negativos)))
