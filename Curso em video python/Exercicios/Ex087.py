'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha'''

matriz = list()
col1 = list()
col2 = list()
col3 = list()
matriz.append(col1)
matriz.append(col2)
matriz.append(col3)
pares = 0
total3 = 0
maior2 = 0
#Inserindo número nas colunas da matriz
for coluna in range(0,3):
    for linha in range(0,3):
        if coluna == 0:
            num = int(input('Digite um número: '))
            if num%2 == 0:
                pares += num
            col1.append(num)
        elif coluna == 1:
            num = int(input('Digite um número: '))
            if num > maior2:
                maior2 = num
            if num%2 == 0:
                pares += num
            col2.append(num)
        elif coluna == 2:
            num = int(input('Digite um número: '))
            if num%2 == 0:
                pares += num
            total3 += num
            col3.append(num)
# Imprimindo a matriz com a formatação correta
print('=========================================================')
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=========================================================')
# Questão A
print(f'A soma de todos os números pares é {pares}')
# Questão B
print(f'A soma de todos os valores da terceira coluna é {total3}')
# Questão C
print(f'O maior valor da segunda coluna é {maior2}')
print('=========================================================')
