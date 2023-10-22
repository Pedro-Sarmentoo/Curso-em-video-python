#Um programa para aprovar um emprestimo bancário. pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da parcela sendo que a parcela não pode ultrapassar 30% do salario dele
valorcasa = int(input('Qual o valor total da casa? '))
tempo = int(input('Em quantos anos pretende pagar a casa? '))
salario = int(input('Qual o seu salário? '))
tempo = tempo * 12
parcela = valorcasa/tempo
if parcela > (salario * 0.3):
    print('Infelizmente o seu pedido de emprestimo foi negado')
else:
    print('Parabens! Seu emprestimo foi aprovado')