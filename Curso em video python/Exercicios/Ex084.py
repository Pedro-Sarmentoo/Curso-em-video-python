'''Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
OBS: caso apareça duas pessoas com o mesmo peso(maior ou menor) mostre o nome das duas'''

# Parte para a coleta dos dados das pessoas
dados = list()
pessoas = list()

while True: 
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = (input('Você deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break
# Parte A:
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')

# Parte B e C:
maiorp = 0
menorp = 200
for p in pessoas:
    if p[1] > maiorp:
        maiorp = p[1]
    if p[1] < menorp:
        menorp = p[1]
# Maior peso
print(f'O maior peso registrado foi {maiorp} Kg de ',end='')
for c in pessoas:
    if c[1] == maiorp:
        print(f'{c[0]}, ',end='')
print('')
# Menor peso
print(f'O menor peso registrado foi {menorp} Kg de ',end='')
for c in pessoas:
    if c[1] == menorp:
        print(f'{c[0]}, ',end='')
print('')