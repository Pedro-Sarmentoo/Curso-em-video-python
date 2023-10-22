#Faça um programa que leia o sexo de uma pessoa mas só aceite M ou F, caso esteje errado peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o seu sexo: ')).strip().lower()[0]

while sexo not in 'mf':
    sexo = str(input('Dado inválido, por favor digite novamente: ')).strip().lower()[0]
print('Sexo {} registrado, obrigado pela colaboração!'.format(sexo.upper()))
