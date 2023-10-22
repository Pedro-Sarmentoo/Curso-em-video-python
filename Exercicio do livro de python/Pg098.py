# Questão 2
par = 0
for c in range (5):
    num = int(input('Digite um número: '))
    if num%2 == 0:
        par += 1
print('Entre esses 5 números, {} são pares'.format(par))
