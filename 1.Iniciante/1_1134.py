alcool = 0
gasolina = 0
diesel = 0
x = int(input())

while x!=1 and x!=2 and x!=3:    
    try:
        x = int(input())
    except EOFError:
        break

    while x==1 or x==2 or x==3 or x==4:
        if x == 1:
            alcool += 1
        elif x == 2:
            gasolina += 1
        elif x == 3:
            diesel += 1
        elif x == 4:
            break
        x = int(input())

print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))