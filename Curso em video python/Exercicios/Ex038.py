#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem--> o primeiro valor é maior, o segundo valor é maior, não existe valor maior, eles são iguais
num1 = int(input('Escreva um número: '))
num2 = int(input('Escreva outro número: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1,num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2,num1))
else:
    print('Os valores são iguais!!')
