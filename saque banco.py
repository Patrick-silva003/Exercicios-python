while True:
    print('          BANCO          ')
    print('=========================')
    valor = int(input('Digite o valor que você deseja sacar: '))
    print('===================================================')
    div50 = valor // 50
    div20 = (valor % 50) // 20
    div10 = (valor % 20) // 10
    div1 = (valor % 10) // 1
    if div50 != 0:
        print(f'Total de cédulas de R$50: {div50}')
    if div20 != 0:
        print(f'Total de cédulas de R$20: {div20}')
    if div10 != 0:
        print(f'Total de cédulas de R$10: {div10}')
    if div1 != 0:
        print(f'Total de cédulas de R$1: {div1}')
    break

