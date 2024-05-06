p = int(input())
w1 = 0
if p>0: 
    q = p%100
    q1 = int(p/100)
else: print("errado")
if q>0:
    r = q%50
    r1 = int(q/50)
else: print("errado")
if r>0:
    s = r%20
    s1 = int(r/20)
else: print("errado")
if s>0:
    t = s%10
    t1 = int(s/10)
else: print("errado")
if t>0:
    u = t%5
    u1 = int(t/5)
else: print("errado")
if u>0:
    v = u%2
    v1 = int(u/2)
else: print("errado")
if v>0:
    w = v%1
    w1 = int(v/1)
print(p)
print("{} nota(s) de R$ 100,00".format(q1))
print("{} nota(s) de R$ 50,00".format(r1))
print("{} nota(s) de R$ 20,00".format(s1))
print("{} nota(s) de R$ 10,00".format(t1))
print("{} nota(s) de R$ 5,00".format(u1))
print("{} nota(s) de R$ 2,00".format(v1))
print("{} nota(s) de R$ 1,00".format(w1))