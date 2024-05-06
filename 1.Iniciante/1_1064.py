a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

valores = [a,b,c,d,e,f]
positivos = []
contagem = []

for i in range(len(valores)):
    if valores[i] > 0:
        positivos.append(valores[i])

for c in range(len(positivos)):
    c += 1
    contagem.append(c)

contagem.sort()
contagem.reverse()

media = sum(positivos)/contagem[0]

print("{} valores positivos".format(contagem[0]))
print("{:.1f}".format(media))


