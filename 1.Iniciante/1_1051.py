x = float(input())
imposto = 0

if x <= 2000.00:
    print("Isento")
else:
    if x > 2000.00 and x <= 3000.00:
        taxa = 0.08
        imposto = (x - 2000.00) * taxa
    if x > 3000.00 and x <= 4500.00:
        taxa = 0.18
        imposto = ((x - 3000.00) * taxa) + (1000.00 * 0.08)
    if x > 4500.00:
        taxa = 0.28
        imposto = ((x - 4500) * taxa) + (1500 * 0.18) + (1000 * 0.08)
    print("R$ {:.2f}".format(imposto))