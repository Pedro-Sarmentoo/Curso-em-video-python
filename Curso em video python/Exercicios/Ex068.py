'''faça um programa que jogue par ou ímpar com o computador. o jogo só será interrompido quando o jogador perder
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.(eu coloco um valor e a maquina outro)
'''
from random import randint

palpites = 0
while True:
    computador = randint(1,2)
    escolha = str(input('Você quer par ou impar: '))
    jogador = int(input('Escolha um número: '))
    resul = computador + jogador
    if escolha == 'par':
        resul = resul%2
        if resul == 0:
            print('Parabens você ganhou!!')
            palpites += 1
        else:
            print('Você perdeu !!')
            break
    if escolha == 'impar':
        resul = resul%2
        if resul != 0:
            print('Parabens você ganhou!!')
            palpites += 1
        else:
            print('Você perdeu !!')
            break
print(f'Você teve {palpites} vitorias consecutivas')
print('Fim')
