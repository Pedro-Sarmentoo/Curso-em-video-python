'''Faça um programa que ajuda um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo(não pode repetir o mesmo número dentro de um jogo), cadastrando tudo em uma lista composta.'''

from random import randint

jogos = int(input('Digite quantos jogos serão gerados: '))
palpite = list()
copypalpite = list()
tdpalpites = list()
tdpalpites.append(copypalpite)
num = 0

for c in range(0,jogos):
    palpite.clear()
    for numeros in range (0,6):
        if numeros == 0:
            num = randint(0,60)
            palpite.append(num)
        else:
            while num in palpite:
                num = randint(0,60)
            palpite.append(num)
    copypalpite.append(palpite[:])
print(tdpalpites)