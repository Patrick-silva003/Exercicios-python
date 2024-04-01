aluno = []
alunos = []
while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    n1 = float(input('Primeira nota: '))
    aluno.append(n1)
    n2 = float(input('Segunda nota: '))
    aluno.append(n2)
    media = (n1 + n2)/2
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    resp = 'j'
    while resp not in 'SN':
        resp = str(input('Quer cadastrar mais alunos? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=======================================================')
print(f'{"N.":<4}{"Aluno":<10}{"Média":>9}')
for c in range(0 ,len(alunos)):
    print(f'{c:<4}{alunos[c][0]:<10}{alunos[c][3]:>8.1f}')
print('=======================================================')
while True:
    notal = int(input('Mostrar notas de qual aluno? (Alunos não numerados interrompe): '))
    if notal in range(0, len(alunos)):
        print(f'As notas de {alunos[notal][0]} foram {alunos[notal][1]} e {alunos[notal][2]}')
        print('====================================================')
    else:
        break


