lista = []
negativos = []

x = int(input())
if x < 0:
    negativos.append(x)
else:
    lista.append(x)

while x > 0:
    x = int(input())    
    if x < 0:
        negativos.append(x)
    else:
        lista.append(x)

soma_total = sum(lista)
elementos = len(lista)

media = soma_total/elementos

print(media)