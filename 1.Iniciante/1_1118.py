x = 0
n = 0
notas = []
while len(notas)!=2:
    x = float(input())
    if 0<=x<=10:
        notas.append(x)
    elif x>10 or x<0:
        print("nota invalida")

media = sum(notas)/len(notas)
print("media = {:.2f}".format(media))

print("novo calculo (1-sim 2-nao)")

while n!=1 and n!=2:
    n = int(input())
    if n!=1 and n!=2:
        print("novo calculo (1-sim 2-nao)")

while n==1:
    notas.clear()
    print("tar")
    while len(notas)!=2:
        x = float(input())
        if 0<=x<=10:
            notas.append(x)
        elif x>10 or x<0:
            print("nota invalida")
    media = sum(notas)/len(notas)
    print("media = {:.2f}".format(media))
    print("novo calculo (1-sim 2-nao)")
    n = int(input())
    if n==1:
        continue
    while n!=1 and n!=2:
        n = int(input())
        if n==1 and n==2:
            pass
        else:
            print("novo calculo (1-sim 2-nao)")