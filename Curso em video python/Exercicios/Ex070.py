'''crie um programa que leia o nome e o preço de vários produtos.
o programa deverá perguntar se o usuário vai continuar,
no final mostre(qual é o total gasto na compra,quantos produtos custam mais de 1000 reais,qual é o nome do produto mais barato)
'''

mais_barato = ''
total = 0
caro = 0
preco_barato = 999999999
while True:
    nome = str(input('Qual o nome do produto: ')).strip()
    preco = int(input('Qual o valor do produto: '))
    total += preco

    if preco > 1000:
        caro += 1
    if preco < preco_barato:
        preco_barato = preco
        mais_barato = nome
        print('Deseja continuar?')
        resp = int(input('Digite 1 para sim e 0 para não: '))
        if resp == 0:
            break
print(f'Sua conta deu no total R$ {total}',end = '')
print(f' sendo {caro} produto(s) acima de R$ 1000 e o mais barato foi o(a) {mais_barato}')

