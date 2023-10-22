#Faça um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
primeiro = float(input('Digite o primeiro termo: '))
razao = float(input('Digite a razão: '))
for c in range (0,11):
    print(primeiro)
    primeiro += razao
