p = float(input())
p_inteira, p_decimal = divmod(p, 1)
p_decimal = p_decimal*100

# Inicializando variáveis
q = r = s = t = u = v = w = 0
b = c = d = e = f = 0

q1 = r1 = s1 = t1 = u1 = v1 = w1 = 0
b1 = c1 = d1 = e1 = f1 = 0

if p_decimal == 0:
  b = 0.0000000000001

#cédulas
if p_inteira>0: 
    q = p_inteira%100
    q1 = int(p_inteira/100)

if q>0:
    r = q%50
    r1 = int(q/50)

if r>0:
    s = r%20
    s1 = int(r/20)

if s>0:
    t = s%10
    t1 = int(s/10)

if t>0:
    u = t%5
    u1 = int(t/5)

if u>0:
    v = u%2
    v1 = int(u/2)

if v>0:
    w = v%1
    w1 = int(v/1)

#moedas
if p_decimal>0:
    b = p_decimal%(0.5*100)
    b1 = int(p_decimal/(0.5*100))

if b>0:
    c = b%(0.25*100)
    c1 = int(b/(0.25*100))

if c>0:
    d = c%(0.1*100)
    d1 = int(c/(0.1*100))

if d>0:
    e = d%(0.05*100)
    e1 = int(d/(0.05*100))

if e>0:
    f = e%(0.01*100)
    f1 = int(e/(0.01*100))
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(q1))
print("{} nota(s) de R$ 50.00".format(r1))
print("{} nota(s) de R$ 20.00".format(s1))
print("{} nota(s) de R$ 10.00".format(t1))
print("{} nota(s) de R$ 5.00".format(u1))
print("{} nota(s) de R$ 2.00".format(v1))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00".format(w1))
print("{:.0f} moeda(s) de R$ 0.50".format(b1))
print("{:.0f} moeda(s) de R$ 0.25".format(c1))
print("{:.0f} moeda(s) de R$ 0.10".format(d1))
print("{:.0f} moeda(s) de R$ 0.05".format(e1))
print("{:.0f} moeda(s) de R$ 0.01".format(f1))