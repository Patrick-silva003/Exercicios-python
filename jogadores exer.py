jogadores = []
jogador = {}
listaquantgol = []
quantgol = 0

while True:
    total = 0
    nome = str(input('Digite o nome do jogador: ')).strip()
    jogador['nome'] = nome
    quantpar = int(input('Quantidade de partidas jogadas: '))
    jogador['partidas'] = quantpar
    for c in range(0, quantpar):
        quantgol = int(input(f'Quantidade de gols da partida {c}: '))
        listaquantgol.append(quantgol)
        total += quantgol
    jogador['gols'] = listaquantgol[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    listaquantgol.clear()
    resp = 'f'
    while resp not in 'SN':
        resp = str(input('Quer adicionar mais jogadores? [S/N] ')).strip().upper()[0]
    print('=' * 40)
    if resp == 'N':
        break
print('='*30)
print(f'{"N.":<4}{"Jogador":<10}{"Gols":>6}{"Total":>9}')
print('='*30)
for c in range(0, len(jogadores)):
    print(f'{c:<4}{jogadores[c]["nome"]:<10}{str(jogadores[c]["gols"]):>8}{str(jogadores[c]["total"]):>5}')
print('='*30)
while True:
    ms = int(input('Mostrar dados de qual jogador? '))
    print('='*30)
    if ms == 999:
        break
    if ms not in range(0, len(jogadores)):
        print('Jogador não existente.')
        break
    else:
        print(F'  -- LEVANTAMENTO DO JOGADOR {jogadores[ms]["nome"]}')
        for c, i in enumerate(jogadores[ms]['gols']):
            print(f'   Na partida {c} marcou {i} gols')
    print('='*30)









