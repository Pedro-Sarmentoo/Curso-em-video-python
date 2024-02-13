'''Crie um programa que tenha uma tupla com nomes de produtos e seus respectivos preços na sequencia. No final, mostre uma listagem de preços organizando os dados em forma tabular.'''

nome = ('Lápis','Borracha','Caderno','Estojo','Transferidor','Compasso','Mochila','Canetas','Livro')

preco = (1.75,2.00,15.90,25.00,4.20,9.99,120.32,22.30,34.90)

print('-' * 50)
print(' ' * 16,'LISTAGEM DE PREÇOS',' ' * 16)
print('-' * 50)

for c in range (0, len(nome)):
    contagem = 0
    contagem = len(nome[c])
    contagem = 38 - contagem
    print('{}'.format(nome[c]),end='')
    print('.' * contagem,'R$ ',end='')
    if preco[c] > 10 and preco[c] < 100:
        print(' ' * 2,end='')
        print('{:.2f}'.format(preco[c]))
    elif preco[c] > 100:
        print(' ' * 1,end='')
        print('{:.2f}'.format(preco[c]))
    else:
        print(' ' * 3,end='')
        print('{:.2f}'.format(preco[c]))

