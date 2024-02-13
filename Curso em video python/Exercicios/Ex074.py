'''Crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla.'''

from random import randint

x1 = randint(0,100)
x2 = randint(0,100)
x3 = randint(0,100)
x4 = randint(0,100)
x5 = randint(0,100)
maior = 0
menor = 101
tupla = (x1,x2,x3,x4,x5)
print(tupla)
for c in range(0, len(tupla)):
  print(tupla[c])
  if maior < tupla[c]:
    maior = tupla[c]
  if menor > tupla[c]:
    menor = tupla[c]
print(f'O maior é {maior}')
print(f'O menor é {menor}')