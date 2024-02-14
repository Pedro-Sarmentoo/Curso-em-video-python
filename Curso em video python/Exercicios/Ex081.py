'''Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso(vai adicionando o quanto quiser), mostre:
A) Quantos números foram digitados
B) A lista de valores ordenada de forma descrescente
C) Se o valor 5 foi digitado e está ou não na lista'''
lista = []
resp = 'a'
n5 = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = input('Você deseja continuar? [S/N] ')
    if resp.upper() == 'N':
        break
print(f'Nesta lista contem {len(lista)} números digitados!')
print('Os valores desta lista em ordem decrescente é: ',end='')
for c in range(0,len(lista)):
    lista.sort(reverse=True)
    print(lista[c],end=', ')
    if lista[c] == 5:
        n5 += 1
print('')
print(f'O número 5 aparece na lista {n5} veze(s)!')