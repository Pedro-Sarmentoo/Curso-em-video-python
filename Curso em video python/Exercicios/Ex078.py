'''Faça um programa que leia 5 valores numericos e guarde-os em uma lista, no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

lista = []
maior = 0
indice1 = 0
indice2 = 0
menor = 1000000
for c in range(0,5):
    lista.append(int(input('Digite um número: ')))
    if lista[c] < menor:
        menor = lista[c]
        indice1 = c
    if lista[c] > maior:
        maior = lista[c]
        indice2 = c
print(f'O maior é: {maior} e está na posição {indice2}')
print(f'O menor é: {menor} e está na posição {indice1}')
print(lista)