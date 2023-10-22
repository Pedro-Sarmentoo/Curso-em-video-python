# Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre quantas pessoas que atigiram a maior idade(21 anos)

from datetime import date

quanti = 0
anoo = date.today().year
lista = []
for c in range(0,7):
    ano = int(input('Digite o ano do seu nascimento: '))
    lista.append(ano)
for c in range(0,7):
    if (anoo - lista[c]) >= 21:
        quanti += 1
print('Ao todo {} pessoas completaram a maior idade!'.format(quanti))
print('No ano de {}'.format(anoo))
