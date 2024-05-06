lista = []
valores = []
inuteis = []

qnt = int(input())

for i in range(qnt):
    a = int(input())
    lista.append(a)

lista.sort()

lista_sem_duplicatas = list(set(lista))
lista_sem_duplicatas.sort()

for c in range(len(lista)):
    try:    
        if lista[c] != lista[c+1]:
            x = lista.count(lista[c])
            valores.append(x)
        elif lista[c] == lista[c+1]:
            y = 1
            inuteis.append(y)
    except IndexError:
        break

for c in range(len(lista)):
        if lista[c] == lista[-1]:
            x = lista.count(lista[c])
            valores.append(x)

for repeticoes in range(len(lista_sem_duplicatas)):
    print(f"{lista_sem_duplicatas[repeticoes]} aparece {valores[repeticoes]} vez(es)")
