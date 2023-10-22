# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
# Ex --> 1 1 2 3 5 8 13 21 

n = int(input('Até qual elemento de fibonacci: '))
num = 1
num0 = 0
aux = 0
limite = 1

while limite <= n:
    print(num)
    aux = num
    num += num0
    num0 = aux
    limite += 1
print('Fim')
