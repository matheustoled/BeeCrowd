x = 0

while x != 2002:
    try:
        x = int(input())
        if x != 2002:
            print("Senha Invalida")
        elif x == 2002:
            print("Acesso Permitido")
    except ValueError:
        break