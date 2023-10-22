#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
num = int(input('Digite um número: '))
x = 0
for c in range(1,11):
    if num/c != 1:
       x += 1
if x > 2:
    print('{} não é um número primo.'.format(num))
else:
    print('{} é um número primo.'.format(num))
