x = int(input())
y = int(input())
mx = max(x,y)
mn = min(x,y)
r = mx-mn

for i in range(mn+1,mx):
    if i%5 == 2 or i%5 == 3:
        print(i)