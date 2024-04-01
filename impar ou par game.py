import random
consec = 0
soma = escmaq = int(0)
while True:
    print('-------------------------------------------')
    print('\033[1;33;40m             Impar ou Par           \033[m')
    print('-------------------------------------------')
    resp = str(input('Você quer ímpar ou par? ')).strip().upper()
    print('-------------------------------------------')
    if resp == 'PAR':
        escolha = int(input('Escolha seu número: '))
        print('Agora o computador escolherá o número dele...')
        print('----------------------------------------------')
        escmaq = random.randint(1, 100)
        soma = int(escolha + escmaq)
        if soma % 2 == 0:
            print(f'O computador jogou {escmaq}')
            print(f'O resultado foi {soma}')
            print('Você venceu! Pronto para outra Rodada?')
            consec += 1
        elif soma % 2 != 0:
            print(f'O computador jogou {escmaq}')
            print(f'O resultado foi {soma} ')
            print('Você perdeu!')
            break
    if resp == 'ÍMPAR':
        escolha = int(input('Escolha seu número: '))
        print('Agora o computador escolherá o número dele...')
        print('---------------------------------------------')
        escmaq = random.randint(1, 100)
        soma = int(escolha + escmaq)
        if soma % 2 != 0:
            print(f'O computador jogou {escmaq}')
            print(f'O resultado foi {soma}')
            print('Você venceu! Pronto para outra Rodada?')
            consec += 1
        elif soma % 2 == 0:
            print(f'O computador jogou {escmaq}')
            print(f'O resultado foi {soma}')
            print('Você perdeu!')
            break
print('-------------------------------------------------------')
print(f'Você adquiriu {consec} vitórias consecutivas!')


























