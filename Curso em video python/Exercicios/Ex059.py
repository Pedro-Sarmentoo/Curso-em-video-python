# :Crie um programa que leia dois valores e mostre um menu, aperte 1 para somar, 2 para multiplicar, 3 para maior, 4 novos numeros, 5 para sair do programa.

v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
x = 0

while x != 5:
    print('===========================================')
    print('                    MENU                   ')
    print('===========================================')
    print('Digite 1 para somar')
    print('Digite 2 para multiplicar')
    print('Digite 3 para descobrir o maior')
    print('Digite 4 para novos valores')
    print('Digite 5 par sair do programa')
    x = int(input())
    if x == 1:
        print('{} + {} = {}'.format(v1,v2,v1+v2))
    elif x == 2:
        print('{} x {} = {}'.format(v1,v2,v1*v2))
    elif x == 3:
        if v1 > v2:
            print('O maior valor é {}'.format(v1))
        else:
            print('O maior valor é {}'.format(v2))
    elif x == 4:
        v1 = int(input('Digite um novo valor: '))
        v2 = int(input('Digite um outro valor: '))
