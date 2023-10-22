''' Crie um programa que leia vários números inteiros pelo teclado.
    o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
    No final,mostre quantos números foram digitados e qual foi a soam entre eles(sem a flag)
'''
quanti = 0
soma = 0
while True:
    num = int(input('Digite um número: '))
    quanti += 1
    soma += num
    if num == 999:
        break
print(f'voce digitou {quanti-1} e a soma de todos ele é igual à {soma-999}')