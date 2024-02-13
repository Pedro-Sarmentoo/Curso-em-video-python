'''Faça um programa que tenha uma tupla com varias palavras, dps tem que mostrar quais vogais tem em cada palavra'''

palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for c in range (0,len(palavras)):# Vai ler todas as palavras da tupla
  palavra = palavras[c]
  print(f'\nNa palavra {palavra} temos',end = ' ')
  for x in range(0,len(palavra)):# Vai ler todas as letras de cada palavra da tupla
    if palavra[x] == 'A':
      print('a',end=' ')
    elif palavra[x] == 'E':
      print('e',end=' ')
    elif palavra[x] == 'I':
      print('i',end=' ')
    elif palavra[x] == 'O':
      print('o',end=' ')
    elif palavra[x] == 'U':
      print('u',end=' ')
    
