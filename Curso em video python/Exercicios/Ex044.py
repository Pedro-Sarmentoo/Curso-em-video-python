#Faça um programa que calcule o valor a ser pago por um produto
#a vista 10% de desconto, a vista no cartao 5% de desconto, em até 2x no cartão é o preço normal e 3 ou mais é 20% de juros
preco = float(input('Qual o valor do produto? '))
forma = str(input('Qual forma de pagamento? '))
if forma == 'dinheiro':
    print('O valor a ser pago é R$ {}'.format(preco - (preco * 0.10)))
elif forma == 'cartao':
    resp = int(input('Irá dividir em quantas vezes? '))
    if resp == 1:
        print('O valor a ser pago é R$ {}'.format(preco - (preco * 0.05)))
    elif resp == 2:
        print('O valor a ser pago é R$ {}'.format(preco))
    else:
        print('O valor a ser pago é R$ {}'.format(preco + (preco * 0.2)))
