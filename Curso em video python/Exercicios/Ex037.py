#Escreva um programa que leia um número inteiro qualquer e peça para o usuário eswcolher qual será a base de conversão, 1 para binario, 2 para octal 3 para hexadecimal
num = int(input('Escreva um número: '))
print('Se você quiser transformar esse número em binário digite 1')
print('Para octal digite 2')
print('Para Hexadecimal digite 3')
escolha = int(input())
if escolha == 1:
    print('O numero {} em binário é {}'.format(num,bin(num)))
elif escolha == 2:
    print('O numero {} em octal é {}'.format(num,oct(num)))
else:
    print('O numero {} em hexadecimal é {}'.format(num,hex(num)))
