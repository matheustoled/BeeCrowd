m = int(input())

meses = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for i in range(0,13):
    if m == i:
        print(meses[i-1])