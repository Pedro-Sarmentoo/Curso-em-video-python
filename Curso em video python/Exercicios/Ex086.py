'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado, no final mostre a matriz na tela com a formatação correta'''

matriz = list()
col1 = list()
col2 = list()
col3 = list()
matriz.append(col1)
matriz.append(col2)
matriz.append(col3)
#Inserindo número nas colunas da matriz
for coluna in range(0,3):
    for linha in range(0,3):
        if coluna == 0:
            num = int(input('Digite um número: '))
            col1.append(num)
        elif coluna == 1:
            num = int(input('Digite um número: '))
            col2.append(num)
        elif coluna == 2:
            num = int(input('Digite um número: '))
            col3.append(num)
# Imprimindo a matriz com a formatação correta
print(matriz[0])
print(matriz[1])
print(matriz[2])

