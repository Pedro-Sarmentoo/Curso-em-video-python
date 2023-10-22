# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando while.

primeiro = int(input('Digite um valor: '))
razao = int(input('Digite a razão: '))
num = 1
while num <= 10:
    print(primeiro)
    primeiro += razao
    num += 1
print('Fim')