# Questão 1
num = int(input('Digite um número: '))
media = 0
for c in range (num):
    num2 = int(input('Digite outro número: '))
    media += num2
media = media/num
print('A media é igual a {}'.format(media))
