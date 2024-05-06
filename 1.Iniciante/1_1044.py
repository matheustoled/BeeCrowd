a,b = map(int, input().split())
# max/min acham o maior e o menor valor entre as variaveis, depois calcula o resto
x = max(a,b)%min(a,b)
if (x==0):
    print("Sao Multiplos")
if (x!=0):
    print("Nao sao Multiplos")