teclas = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'

while True:
    try:
        frase = input()
        traducao = ''
        for i in frase:
            if i == ' ':
                traducao += i
            else:
                x = teclas[teclas.index(i) - 1]
                traducao += x
        print(traducao)
    except EOFError:
        break