# um programa que leia varios numeros inteiros pelo teclado, o programa só ira parar quando o usuário digitar o valor 999, que é a condição de parada
# no final mostre quantos números foram digitados e qual foi a soma entre eles sem contar o (999)

x = 0
total = 0
quanti = 0

while x != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        x = 999
        num = 0
        quanti -= 1
    total += num
    quanti += 1
print('A soma de todos os números é: {}'.format(total))
print('A quantidade de números digitados foi {}'.format(quanti))
print('Fim')
