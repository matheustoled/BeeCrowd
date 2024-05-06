N = int(input())
valores = []

for i in range(0,10):
    v = (i+1)*N
    valores.append(v)

for p in range(len(valores)):
    v = (p+1)*N
    print("{} x {} = {}".format(p+1,N ,v))
