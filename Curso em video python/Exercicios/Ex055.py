# Faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o maior e menor peso

maior = 0
menor = 1000
for c in range (0,5):
    peso = float(input('Digite o seu peso: '))   
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior,menor))
