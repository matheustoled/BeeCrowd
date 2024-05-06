hi,mi,hf,mf = map(int, input().split())
tempo_i = (hi*60) + mi
tempo_f = (hf*60) + mf

if tempo_f > tempo_i:
    duracao = tempo_f - tempo_i
elif tempo_f < tempo_i:
    duracao = (1440 - tempo_i) + tempo_f
elif tempo_f == tempo_i:
    duracao = 1440

horas = duracao//60
minutos = (duracao%60)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))


