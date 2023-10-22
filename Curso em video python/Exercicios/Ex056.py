# Faça um programa que leia o nome, idade e sexo de 4 pessoas e no final mostre a media de idade
# qual nome do homem mais velho e quantas mulheres tem menos de 21 anos

lista_nome = []
lista_sexo = []
lista_idade = []
media_idade = 0
velho = 0
marc = 0
marc2 = 0

for c in range(0,4):
    nome = str(input('Digite o seu nome: '))
    sexo = str(input('Qual o seu sexo: ').lower())
    idade = int(input('Qual a sua idade: '))
    lista_nome.append(nome)
    lista_sexo.append(sexo)
    lista_idade.append(idade)

for c in range(0,4):
    media_idade += lista_idade[c]
    if lista_sexo[c] == 'm':
        if lista_idade[c] > velho:
            velho = lista_idade[c]
            marc = c
    if lista_sexo[c] == 'f':
        if lista_idade[c] > 21:
            marc2 += 1

media_idade = media_idade/4
print('A média das idades é {} anos'.format(media_idade))
print('O nome do homem mais velho é {}'.format(lista_nome[marc]))
print('E existe(m) {} mulhere(s) com mais de 21 anos'.format(marc2))
