A,B,C = map(float, input().split())
lista = [A,B,C]
lista.sort()
lista.reverse()
A, B, C = lista

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B  and C != A or C == A and B!=A or C == B and B != A:
        print("TRIANGULO ISOSCELES")