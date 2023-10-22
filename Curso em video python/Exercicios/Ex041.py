# Um programa que leia o ano de nascimento e mostre a categoria de acordo com sua idade, até 9 mirim, até 14 infantil, até 19 junior, até 20 senior e acima master
idade = int(input('Qual a sua idade? '))
if idade <= 9 :
    print('Categoria Mirim!')
elif idade > 9 and idade <= 14 :
    print('Categoria Infantil!')
elif idade > 14 and idade <= 19 :
    print('Categoria Junior!')
elif idade > 19 and idade <= 20 :
    print('Categoria Senior!')
else :
    print('Categoria Master!')
