from math import pow, sqrt

lista = []
media = soma = 0
quadrados = []
soma_quad = variancia = desvio_padrao = 0
n = int(input('Quantos números você quer usar para calcular o desvio padrão? '))

for c in range(n):
    lista.append(int(input('Digite um valor: ')))
    soma += lista[c]

media = soma / n
for c in range(n):
    quadrados.append(pow(lista[c] - media, 2))
    soma_quad += quadrados[c]

variancia = soma_quad / n
desvio_padrao = sqrt(variancia)

print(f'{desvio_padrao:,.2f}')













