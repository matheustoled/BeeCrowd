impares = []

x = int(input())
y = int(input())

mx = max(x,y)
mn = min(x,y)

while mx > mn:
  if x%2 == 0:
    x =+ 1
  else:
    impares.append(x)
    
while mx > mn:
  if y%2 == 0:
    y =+ 1
  else:
    impares.append(y)

sum.impares
print(impares)