# Melhore o jogo do desafio 028 onde o computador vai "pensar" em un número entre 0 e 10.Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites teve

from random import randint

numero = randint(1,10)
palpite = False
chances = 0

while not palpite:
    jogador = int(input('Em qual número estou pensando de 1 até 10: '))
    chances += 1
    if jogador > numero:
        print('É menor')
    else:
        print('É maior')
    if jogador == numero:
        palpite = True
print('Acertou, depois de {} tentativas'.format(chances))
