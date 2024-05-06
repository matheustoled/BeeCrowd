qnt = int(input())
nome = 0

for i in range(qnt):
    lista = list(map(str, input().split()))
    nome = lista[0]
    if nome == "Thor":
        print("Y")
    else:
        print("N")