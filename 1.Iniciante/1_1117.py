x = 0
notas = []
while len(notas)!=2:
    x = float(input())
    if 0<=x<=10:
        notas.append(x)
    elif x>10 or x<0:
        print("nota invalida")

media = sum(notas)/len(notas)
print(f"media = {media}")