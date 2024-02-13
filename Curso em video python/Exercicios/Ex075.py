'''Faça um programa que leia 4 valores e guarde em uma tupla e no final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor.
C) Quais foram os números pares.'''

v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
v3 = int(input('Digite o 3º valor: '))
v4 = int(input('Digite o 4º valor: '))
n9 = 0
pos = 0
par = 0
tupla = (v1,v2,v3,v4)

for c in range(0,len(tupla)):
  if tupla[c] == 9 and n9 == 0:
    pos = c
  if tupla[c] == 9:
    n9 = n9 + 1
  if tupla[c]%2 == 0:
    par = par + 1
print(f'O número 9 apareceu {n9} vezes')
print(f'O número 9 apareceu na primeira vez na posição {pos}')
print(f'Na tupla existe(m) {par} números pares')

