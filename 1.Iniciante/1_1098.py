I = 0
J = 1

while I <= 2:
    for i in range(3):
        if I == int(I):
            print("I={:.0f} J={:.0f}".format(I,J))
        else:
            print("I={:.1f} J={:.1f}".format(I,J))
        J += 1.0
    I = round(I + 0.2, 1)
    J = round(J - 2.8, 1)