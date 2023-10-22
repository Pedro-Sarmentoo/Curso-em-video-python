'''Ex071: Crie um programa que simule o funcionamento de um caixa eletrônico.
 No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas células de cada valor serão entregues. OBS: considere que o caixa possui cédulas de 50,20,10 e 1 real(reais).
'''
def menu():
    print('==========================================')
    print('             CAIXA ELETRÔNICO             ')
    print('==========================================')

n100 = int(0)
n50 = int(0)
n20 = int(0)
n10 = int(0)
n1 = int(0)

while True:
    saque = int(input('Quanto será sacado: '))
    if saque >= 100:
        n100 = saque/100
        saque -= (n100*100)
    if saque != 0 and saque >= 50:
        n50 = saque/50
        saque -= (n50*50)
    if saque != 0 and saque >= 20:
        n20 = saque/20
        saque -= (n20*20)
    if saque != 0 and saque >= 10:
        n10 = saque/10
        saque -= (n10*10)
    if saque < 10:
        break
print(f'{n100} cédulas de 100 reais')
print(f'{n50} cédulas de 50 reais')
print(f'{n20} cédulas de 20 reias')
print(f'{n10} cédulas de 10 reais')
print(f'{n1} moedas de 1 real')
    