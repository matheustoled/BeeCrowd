qnt_testes = int(input())
total_cobaias = []
coelhos_totais = 0
ratos_totais = 0
sapos_totais = 0

for i in range(qnt_testes):
    qnt_cobaias, tipo_cobaias = map(str, input().split())
    qnt_cobaias = int(qnt_cobaias)
    total_cobaias.append(qnt_cobaias)
    if tipo_cobaias == "C":
        coelhos_totais += qnt_cobaias
    elif tipo_cobaias == "R":
        ratos_totais += qnt_cobaias
    elif tipo_cobaias == "S":
        sapos_totais += qnt_cobaias

soma_total_cobaias = sum(total_cobaias)

coelhos_percentual = ((coelhos_totais*100)/soma_total_cobaias)
ratos_percentual = ((ratos_totais*100)/soma_total_cobaias)
sapos_percentual = ((sapos_totais*100)/soma_total_cobaias)

print("Total: {} cobaias".format(soma_total_cobaias))

print("Total de coelhos: {}".format(coelhos_totais))
print("Total de ratos: {}".format(ratos_totais))
print("Total de sapos: {}".format(sapos_totais))

print("Percentual de coelhos: {:.2f} %".format(coelhos_percentual))
print("Percentual de ratos: {:.2f} %".format(ratos_percentual))
print("Percentual de sapos: {:.2f} %".format(sapos_percentual))