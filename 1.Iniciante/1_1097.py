I = 1
J = 7
i = 0
c = 1

while c < 6:
    for i in range(3):
        print("I={} J={}".format(I,J))
        J -= 1
    I += 2 
    J += 5
    c += 1