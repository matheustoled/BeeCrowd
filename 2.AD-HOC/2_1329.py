while 1:
    x = int(input())
    if x != 0:
        lista = list(map(int, input().split()))
        caras = 0 #Mary -> 0
        coroas = 0 #john -> 1
        for i in range(x):
            if lista[i] == 0:
                caras += 1
            else:
                coroas += 1
        print("Mary won {} times and John won {} times".format(caras,coroas))
    else:
        break