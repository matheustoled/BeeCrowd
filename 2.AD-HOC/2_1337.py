a = 1
b=a
c=a
while a!=0 and b!=0 and c!=0:
    lista = list(map(int, input().split()))
    lista.sort()
    a = lista[0]
    b = lista[1]
    c = lista[2]
    #caso que finaliza o jogo
    if a==0 and b==0 and c==0:
        break
    #sets
    elif a!=13 and a==b and b==c and c==a:
        print("{} {} {}".format(a+1,b+1,c+1))
    elif a==13 and a==b and b==c and c==a:
        print("*")
    #pares
    elif c!=13 and a==b and b!=c:#menores que a carta avulsa.Ex.: 1 1 12
        print("{} {} {}".format(a,b,c+1))
    elif c==13 and a==b and b!=c:#menores que a carta avulsa.Ex.: 1 1 13
        print("{} {} {}".format(c-12,a+1,b+1))
    elif c!=13 and a!=b and b==c and b-a==1:#maiores que a carta avulsa.Ex.: 1 2 2 #b-a==1
        print("{} {} {}".format(b,c,a+2))
    elif c!=13 and a!=b and b==c and b-a>=2:#maiores que a carta avulsa.Ex.: 1 2 2 #b-a>=2
        print("{} {} {}".format(a+1,b,c))
    elif c==13 and a==12 and a!=b and b==c:#maiores que a carta avulsa.Ex.: 12 13 13
        print("{} {} {}".format(1,1,1))
    elif c==13 and a!=b and b==c:#maiores que a carta avulsa.Ex.: 12 13 13
        print("{} {} {}".format(a+1,b,c))
    #não-pares
    elif a!=b and b!=c and c!=a:
        print("{} {} {}".format(1,1,2))