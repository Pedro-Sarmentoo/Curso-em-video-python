'''Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, cire duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final mostre o conteudo das tres listas geradas'''
lista = []
listap = []
listai = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = input('Você deseja continuar? [S/N] ')
    if resp.upper() == 'N':
        break
for c in range (0,len(lista)):
    if lista[c]%2 == 0:
        listap.append(lista[c])
    else:
        listai.append(lista[c])
print(f'Lista geral {lista}')
print(f'Lista dos pares {listap}')
print(f'Lista dos impares {listai}')