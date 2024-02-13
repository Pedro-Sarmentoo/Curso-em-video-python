'''Crie um programa onde o usuario possa digitar varios(o usuario decide quando terminar de adicionar numeros) valores numericos e cadadestre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores unicos digitados em ordem crescente'''

lista = []
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Esse número já foi inserido!')
    else:
        lista.append(num)
    #Saida do laço while
    resp = input('Você deseja continuar? [S/N]: ')
    if resp.upper() == 'N':
        break
    
print('A lista em ordem crescente é: ',end='')
lista.sort()
print(lista)