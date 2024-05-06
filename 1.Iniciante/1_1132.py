x = int(input())
y = int(input())
mx = max(x,y)
mn = min(x,y)
r = mx-mn
nao_multiplos = []

for i in range(r+1):
    if (mn+i)%13 != 0:
        nao_multiplos.append(mn+i)

soma = sum(nao_multiplos)

print(soma)