lispess = []
dictpess = {}
quantpess = tot = media = 0
while True:
    nome = str(input('Digite o nome: ')).strip()
    dictpess['nome'] = nome
    idade = int(input('Digite a idade: '))
    dictpess['idade'] = idade
    sexo = 'f'
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    dictpess['sexo'] = sexo
    lispess.append(dictpess.copy())
    dictpess.clear()
    quantpess += 1
    tot += idade
    resp = 'f'
    while resp not in 'SN':
        resp = str(input('Quer cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
media = tot / quantpess
feminino = []
altmed = []
altmeddic = {}
for c in range(0, len(lispess)):
    if lispess[c]['sexo'] == 'F':
        feminino.append(lispess[c]['nome'])
    if lispess[c]['idade'] > media:
        altmeddic['nome'] = lispess[c]['nome']
        altmeddic['idade'] = lispess[c]['idade']
        altmed.append(altmeddic.copy())
        altmeddic.clear()
print('-=-'*20)
print(f' -Total de pessoas: {quantpess}')
print(f' -Média de idade: {media} anos')
print(f' -Mulheres do grupo: {feminino[:]}')
print('Pessoas com idade acima da Média: ')
for c in range(0, len(altmed)):
    print(f'{altmed[c]["nome"]} com {altmed[c]["idade"]} anos')








