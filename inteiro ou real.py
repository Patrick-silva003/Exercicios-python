def inteiro():
    while True:
        n = ''
        try:
            n = str(input('Digite um número inteiro: ')).strip()
            int(n)
            break
        except (ValueError, TypeError):
            print('\033[0;31mErro! Número Inválido.\033[m')
        except KeyboardInterrupt:
            n = 0
            print('\033[0;31mO usuário não quis fornencer mais dados\033[m')
            break
    return n


def real():
    while True:
        j = ''
        try:
            j = str(input('Digite um número real: ')).strip()
            float(j)
            break
        except (ValueError, TypeError):
            print('\033[0;31mErro! Número Inválido.\033[m')
        except KeyboardInterrupt:
            j = 0
            print('\033[0;31mO usuário não quis fornecer mais dados\033[m')
            break
    return j


i = inteiro()
r = real()
print(f'O número inteiro digitado foi {i}, o real foi {r}')






