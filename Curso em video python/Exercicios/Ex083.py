'''Crie um programa onde o usuario digita uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta'''

op = input('Digite a expressão: ')
lista = op[:]
achou = False
errado = True
for c in range(0,len(lista)):
    if lista[c] == '(':
        achou = True
    elif lista[c] == ')' and achou == True:
        errado = False
if achou == True and errado == False:
    print('A expressão está correta!!')
else:
    print('A expressão está incorreta')