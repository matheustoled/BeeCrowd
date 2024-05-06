qnt = int(input())
impares = []

for i in range(qnt):
    x, y = map(int, input().split())
    mx = max(x, y)
    mn = min(x, y)
    mn += 1
    while mn < mx:
        if mn%2 != 0:
            impares.append(mn)
        mn += 1
    soma_impares = sum(impares)
    print(soma_impares)
    impares.clear()