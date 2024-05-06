i = int(input().strip("Dia "))
h1, m1, s1 = map(int, input().split(" : "))

f = int(input().strip("Dia "))
h2, m2, s2 = map(int, input().split(" : "))

h1 = h1 * 3600
h2 = h2 * 3600

m1 = m1 * 60
m2 = m2 * 60

tti = h1 + m1 + s1
ttf = h2 + m2 + s2

dias = (f - i) * 86400

if tti >= ttf:
    segundos = dias - (tti - ttf)
else:
    segundos = dias + (ttf - tti)

w = segundos//86400
w1 = segundos%86400
x = w1//3600
x1 = w1%3600
y = x1//60
y1 = x1%60
z = y1

print("{} dia(s)".format(w))
print("{} hora(s)".format(x))
print("{} minuto(s)".format(y))
print("{} segundo(s)".format(z))