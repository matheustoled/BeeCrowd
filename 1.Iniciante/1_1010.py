# o "split()" transforma tudo em string e depois o "map(float)" transforma as strings em float
c1, u1, p1 = map(float, input().split())
c2, u2, p2 = map(float, input().split())
total = u1 * p1 + u2 * p2
print("VALOR A PAGAR: R$ {:.2f}".format(total))