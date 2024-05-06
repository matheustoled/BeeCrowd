a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

valores = [a,b,c,d,e,f]
positivos = []
organizar = []
qnt_termos = []

for i in range(len(valores)):
    if valores[i] > 0:
        positivos.append(valores[i])

for c in range(len(positivos)):
    organizar.append(c)

organizar.sort()
organizar.reverse()

qnt_termos = organizar[0] + 1

print(f"{qnt_termos} valores positivos")