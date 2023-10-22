#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
total = 0
for c in range(0,7):
    num = int(input('Digite um número: '))
    if num%2 == 0:
        total += num
print('A soma de todos os números pares {}'.format(total))
