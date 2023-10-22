# Crie um programa que leia varios numeros pelo teclado, no final da execução mostre a media entre todos os valores e qual foi o maior e o menor numero
# o programa deve perguntar se ele quer continuar ou não a digitar valores.

resp = 's'
maior = 0
menor = 999999999999999
media = 0
quanti = 0

while resp != 'n':
    num = int(input('Digite um número: '))
    media += num
    quanti += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = str(input('Voce deseja continuar? [S/N] '))
media = (media/quanti)
print('A média é {}'.format(media))
print('O maior foi {} e o menor foi {}'.format(maior,menor))
