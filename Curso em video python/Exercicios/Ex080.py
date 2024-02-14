'''Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição correta de inserção sem usar o SORT, no final mostre a lista ordenada na tela'''

lista = []
for c in range(0,5):
    num = int(input('Digite um número: '))
    if c == 0:
        lista.append(num)
    else:
        posicao = 0
        for x in range(0,len(lista)):
            if num > lista[x]:
                posicao += 1
        lista.insert(posicao,num)
print(lista)