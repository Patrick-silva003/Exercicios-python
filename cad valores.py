listanum = []
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado!')
    else:
        if n in listanum:
            print('Valor já existente!')
    resp = 'f'
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
listanum.sort()
print(f'Você digitou os valores: {listanum}')













