a,b,c = map(int, input().split())
valores1 = [a,b,c]
valores2 = sorted(valores1)

#aqui não usei o "len" pois já defini a quantidade de elementos da lista 
for i in range(3):
    print(valores2[i])

print() #Espaço em branco

#o "len" conta sozinho quantos elementos tem na lista
for i in range(len(valores2)):
    print(valores1[i])