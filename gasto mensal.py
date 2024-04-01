print('          GASTO MENSAL          ')
print('--------------------------------')
cont = 1
gasto = caro = barato = 0
nomebara = ''
while True:
    nomeprod = str(input('Digite o nome do produto: ')).strip().upper()
    preçoprod = float(input('Digite o preço do produto: '))
    print('-----------------------------------------------------')
    gasto += preçoprod
    if cont == 1:
        barato = preçoprod
        nomebara = nomeprod
    else:
        if preçoprod < barato:
            barato = preçoprod
            nomebara = nomeprod
    if preçoprod > 1000:
        caro += 1
    cont += 1
    resp = str(input('Quer digitar mais produtos? [S/N] ')).strip().upper()
    print('-------------------------------------------------------------')
    if resp == 'N':
        break
print(f'O gasto mensal foi de {gasto} reais')
print(f'Produtos que custaram mais de 1000 reais: {caro}')
print(f'O produto mais barato foi o[a] {nomebara}')




