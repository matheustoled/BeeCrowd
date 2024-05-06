import math

r, l = map(int, input().split())
pi = 3.1415
v = 4/3*pi*r**3
baloes = l/v
print(math.floor(baloes))